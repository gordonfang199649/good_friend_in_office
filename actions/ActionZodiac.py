import re
from functools import lru_cache
import requests
from bs4 import BeautifulSoup

from linebot.models import TextSendMessage, QuickReply, QuickReplyButton, MessageAction

from common.LoadEnvVariable import SIGN_ZODIAC_URL, ARIES_PICTURE, TAURUS_PICTURE, GEMINI_PICTURE, CANCER_PICTURE, \
    LEO_PICTURE, VIRGO_PICTURE, LIBRA_PICTURE, SCORPIO_PICTURE, SAGITTARIUS_PICTURE, CAPRICORN_PICTURE, \
    AQUARIUS_PICTURE, PISCES_PICTURE
from messages.MessageZodiacReply import reply_zodiac_not_exists, reply_question
from templates.TodayFortuneTemplate import today_fortune_template

# 星座轉換字典
zodiacSigns_convert = {
    re.compile('牡羊座'): 'Aries',
    re.compile('金牛座'): 'Taurus',
    re.compile('雙子座'): 'Gemini',
    re.compile('巨蟹座'): 'Cancer',
    re.compile('獅子座'): 'Leo',
    re.compile('處女座'): 'Virgo',
    re.compile('天秤座'): 'Libra',
    re.compile('天蠍座'): 'Scorpio',
    re.compile('射手座'): 'Sagittarius',
    re.compile('摩羯座'): 'Capricorn',
    re.compile('水瓶座'): 'Aquarius',
    re.compile('雙魚座'): 'Pisces'
}

"""
    詢問使用者是什麼星座
    :param str: 原始訊息
    :param pattern: 正規表達式
    :return Line 訊息封裝物件
"""
def ask_users_zodiac_sign(intent: str, pattern: re) -> QuickReply:
    quick_reply = QuickReply(items=[
        QuickReplyButton(image_url=ARIES_PICTURE, action=MessageAction(label="牡羊座今日運勢", text="牡羊座")),
        QuickReplyButton(image_url=TAURUS_PICTURE, action=MessageAction(label="金牛座今日運勢", text="金牛座")),
        QuickReplyButton(image_url=GEMINI_PICTURE, action=MessageAction(label="雙子座今日運勢", text="雙子座")),
        QuickReplyButton(image_url=CANCER_PICTURE, action=MessageAction(label="巨蟹座今日運勢", text="巨蟹座")),
        QuickReplyButton(image_url=LEO_PICTURE, action=MessageAction(label="獅子座今日運勢", text="獅子座")),
        QuickReplyButton(image_url=VIRGO_PICTURE, action=MessageAction(label="處女座今日運勢", text="處女座")),
        QuickReplyButton(image_url=LIBRA_PICTURE, action=MessageAction(label="天秤座今日運勢", text="天秤座")),
        QuickReplyButton(image_url=SCORPIO_PICTURE, action=MessageAction(label="天蠍座今日運勢", text="天蠍座")),
        QuickReplyButton(image_url=SAGITTARIUS_PICTURE, action=MessageAction(label="射手座今日運勢", text="射手座")),
        QuickReplyButton(image_url=CAPRICORN_PICTURE, action=MessageAction(label="摩羯座今日運勢", text="摩羯座")),
        QuickReplyButton(image_url=AQUARIUS_PICTURE, action=MessageAction(label="水瓶座今日運勢", text="水瓶座")),
        QuickReplyButton(image_url=PISCES_PICTURE, action=MessageAction(label="雙魚座今日運勢", text="雙魚座")),
    ])
    return TextSendMessage(text=reply_question(), quick_reply=quick_reply)

"""
    查詢星座今日運勢
    :param str: 原始訊息
    :param pattern: 正規表達式
    :return Line 訊息封裝物件
"""
def get_today_fortune(intent: str, pattern: re):
    url = None
    for pattern, sign_name in zodiacSigns_convert.items():
        matched = pattern.match(intent)
        if matched:
            url = f'{SIGN_ZODIAC_URL}{sign_name}'

    # 使用者輸入星座不存在，要求使用者重新輸入
    if url is None:
        reply_messages = [TextSendMessage(text=reply_zodiac_not_exists()),
                          ask_users_zodiac_sign(intent='', pattern=None)]
        return reply_messages

    return crawl_zodiac_sign_website(url=url)

"""
    使用爬蟲爬星座網站
    快取 12 個星座，當查詢相同星座，不需要爬星座網站
    :param url: 星座網站網址
    :return Line 訊息封裝物件
"""
@lru_cache(maxsize=12)
def crawl_zodiac_sign_website(url):
    response = requests.get(url)
    response.encoding = 'UTF-8'
    if response.status_code == requests.codes.ok:
        sp = BeautifulSoup(response.text, 'html.parser')
        # 將爬蟲物件 Pass 給模板，讓方法把解析的資料填進去模板
        return today_fortune_template(sp)
    else:
        # Http Response code 非 200，直接拋錯，回覆使用網站異常
        raise Exception
