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
from intents.IntentDispatcher import dispatch

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
    LOGGER.info(f'Line 使用者傳送訊息: {event.message.text}')
    try:
        profile = line_bot_api.get_profile(event.source.user_id)
        LOGGER.info(f'Line 使用者 ID: {profile.user_id}')
        LOGGER.info(f'Line 使用者顯示名稱: {profile.display_name}')
    except Exception as e:
        LOGGER.info(f'使用者 {event.source.user_id} 目前不是好友')

    reply_message = dispatch(intent=event.message.text)
    if reply_message is not None:
        line_bot_api.reply_message(event.reply_token, reply_message)

if __name__ == "__main__":
    app.run()
