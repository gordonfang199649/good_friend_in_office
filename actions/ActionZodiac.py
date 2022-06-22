import re

import requests
from bs4 import BeautifulSoup

from linebot.models import FlexSendMessage, TextSendMessage

from common.LoadEnvVariable import SIGN_ZODIAC_URL
from templates.TodayFortuneTemplate import today_fortune_template

# 星座轉換字典
zodiacSigns_convert = {
    re.compile('.*牡羊座?.*'): 'Aries',
    re.compile('.*金牛座?.*'): 'Taurus',
    re.compile('.*雙子座?.*'): 'Gemini',
    re.compile('.*巨蟹座?.*'): 'Cancer',
    re.compile('.*獅子座?.*'): 'Leo',
    re.compile('.*處女座?.*'): 'Virgo',
    re.compile('.*天秤座?.*'): 'Libra',
    re.compile('.*天蠍座?.*'): 'Scorpio',
    re.compile('.*射手座?.*'): 'Sagittarius',
    re.compile('.*摩羯座?.*'): 'Capricorn',
    re.compile('.*水瓶座?.*'): 'Aquarius',
    re.compile('.*雙魚座?.*'): 'Pisces'
}

"""
    查詢星座今日運勢
    :param str: 原始訊息
    :param pattern: 正規表達式
    :return Line 訊息封裝物件
"""

def get_today_fortune(intent: str, pattern: re) -> FlexSendMessage or TextSendMessage:
    url = None
    for pattern, sign_name in zodiacSigns_convert.items():
        matched = pattern.match(intent)
        if matched:
            url = f'{SIGN_ZODIAC_URL}{sign_name}'

    if url is None:
        return TextSendMessage(text='您輸入的星座不存在耶，要不要再重新輸入一次')

    response = requests.get(url)
    response.encoding = 'UTF-8'
    if response.status_code == requests.codes.ok:
        sp = BeautifulSoup(response.text, 'html.parser')
        # 將爬蟲物件 Pass 給模板，讓方法把解析的資料填進去模板
        return today_fortune_template(sp)
    else:
        # Http Response code 非 200，直接拋錯，回覆使用網站異常
        raise Exception
