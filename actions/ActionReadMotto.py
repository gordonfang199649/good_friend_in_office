import re
from opencc import OpenCC
import requests
from linebot.models import TextSendMessage
from common.LoadEnvVariable import MOTTO_URL

"""
    讀今日金句名言
    :param str: 原始訊息
    :param pattern: 正規表達式
    :return Line 訊息封裝物件
"""

def read_motto(intent: str, pattern: re) -> TextSendMessage:
    response = requests.get(MOTTO_URL)
    response.encoding = 'UTF-8'
    if response.status_code == requests.codes.ok:
        # 將文字從簡體字轉成繁體字
        cc = OpenCC('s2twp')
        return TextSendMessage(text=cc.convert(text=response.json()['data']['content']))
    else:
        # Http Response code 非 200，直接拋錯，回覆使用網站異常
        raise Exception
