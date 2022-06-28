import importlib
import sys
import traceback

from linebot.models import TextSendMessage
import config.Logger
import logging as LOGGER

from domains.dictionaries.DomainDictionary import patterns
from models.UserContext import UserContext

"""
    intent - 使用者意圖領域判斷
    :author Gordon Fang
    :date 2022-06-27
"""

"""
    分派機器人回應的動作
    :param intent: 原始訊息
    :param cache: 注入進來的快取器
    :return Line 訊息封裝物件
"""

def dispatch(user_context: UserContext):
    for pattern, intent in patterns.items():
        matched = pattern.match(user_context.message.message)

        # 若無命中任一意圖，機器人則不回應訊息
        if matched:
            if intent[0] not in sys.modules:
                importlib.import_module(intent[0])
            try:
                user_context.message.domain = intent[0]
                return getattr(sys.modules[intent[0]], intent[1])(user_context=user_context)
            except Exception as e:
                traceback.print_exc()
                LOGGER.error(e)
                return TextSendMessage(text='很抱歉，服務異常，請聯絡開發人員。')

    return None
