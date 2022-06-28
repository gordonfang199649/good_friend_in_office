import logging as LOGGER
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage
)

from common.LoadEnvVariable import CHANNEL_ACCESS_TOKEN, CHANNEL_SECRET
from domains.DomainDispatcher import dispatch
from models.Message import Message
from models.UserContext import UserContext
from utils.MessageCache import cache

"""
    configurations
"""
LOGGER.getLogger(__name__)

"""
    全域變數
"""
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)
app = Flask(__name__)
message_cache = cache
"""
    call back function
"""

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    LOGGER.info(f"Request body: {body}")

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        LOGGER.error("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

"""
    處理 Line 文字訊息
    :param event: 事件
"""

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    LOGGER.debug(f'Line 使用者傳送訊息: {event.message.text}')

    message = Message()
    message.original_message = event.message.text
    if event.source.user_id not in message_cache.keys():
        message_cache[event.source.user_id] = []
    message_cache[event.source.user_id].insert(0, message)

    user_context = UserContext()
    user_context.user_id = event.source.user_id
    user_context.message = message
    reply_message = dispatch(user_context=user_context)

    if reply_message is not None:
        line_bot_api.reply_message(event.reply_token, reply_message)

if __name__ == "__main__":
    app.run()
