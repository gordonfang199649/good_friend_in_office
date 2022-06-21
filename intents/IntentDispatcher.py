import importlib
import sys
import traceback

from linebot.models import TextSendMessage
import config.Logger
import logging as LOGGER

from intents.dictionaries.IntentDictionary import patterns

"""
    intent - 使用者意圖判斷
    :author Gordon Fang
    :date 2022-06-11
"""

"""
    分派機器人回應的動作
    :param intent: 原始訊息
    :param cache: 注入進來的快取器
    :return Line 訊息封裝物件
"""

def dispatch(intent: str):
    for pattern, action in patterns.items():
        matched = pattern.match(intent)

        # 若無命中任一意圖，機器人則不回應訊息
        if matched:
            if action[0] not in sys.modules:
                importlib.import_module(action[0])
            try:
                return getattr(sys.modules[action[0]], action[1])(intent=intent, pattern=pattern)
            except Exception as e:
                traceback.print_exc()
                LOGGER.error(e)
                return TextSendMessage(text='很抱歉，服務異常，請聯絡開發人員。')

    return None
