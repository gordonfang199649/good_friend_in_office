from bs4 import BeautifulSoup
from linebot.models import (
    FlexSendMessage
)

from common.LoadEnvVariable import SIGN_ZODIAC_ROOT_URL, SIGN_ZODIAC_MOOD_THUNDER, SIGN_ZODIAC_MOOD_CLOUDY, \
    SIGN_ZODIAC_MOOD_RAIN, SIGN_ZODIAC_MOOD_PARTLY_CLOUDY, SIGN_ZODIAC_MOOD_SUNNY

"""
    產製今日星座運勢模板
"""

def today_fortune_template(sp: BeautifulSoup) -> FlexSendMessage:
    # 星座名稱
    zodiacSigns_name = sp.select(".middle .name .name")[0].text
    # 星座日期
    zodiacSigns_date = sp.select(".middle .name .date")[0].text
    # 今日心情
    today_horoscope_weather = sp.select(".today .weather")[0].text
    # 星座圖片
    zodiac_picture = f"{SIGN_ZODIAC_ROOT_URL}{sp.select('.horoscope img')[0].attrs['src']}"
    # 今日運勢
    today_horoscope = sp.select("section article")[0].text.lstrip()

    today_mood_picture = None
    if len(sp.select('.thunder')):
        today_mood_picture = SIGN_ZODIAC_MOOD_THUNDER
    elif len(sp.select('.cloudy')):
        today_mood_picture = SIGN_ZODIAC_MOOD_CLOUDY
    elif len(sp.select('.rain')):
        today_mood_picture = SIGN_ZODIAC_MOOD_RAIN
    elif len(sp.select('.partly_cloudy')):
        today_mood_picture = SIGN_ZODIAC_MOOD_PARTLY_CLOUDY
    elif len(sp.select('.sunny')):
        today_mood_picture = SIGN_ZODIAC_MOOD_SUNNY

    contents = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": today_mood_picture,
                            "size": "full",
                            "aspectMode": "cover",
                            "gravity": "center",
                            "flex": 1,
                            "aspectRatio": "3:1"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": today_horoscope_weather,
                                    "color": "#FFFFFF",
                                    "weight": "bold",
                                    "style": "normal",
                                    "size": "xxl"
                                }
                            ],
                            "position": "absolute",
                            "offsetTop": "xxl",
                            "offsetStart": "xxl"
                        }
                    ]
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "image",
                                    "url": zodiac_picture,
                                    "aspectMode": "cover",
                                    "size": "full"
                                }
                            ],
                            "cornerRadius": "100px",
                            "width": "72px",
                            "height": "72px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": f'{zodiacSigns_name}今日運勢',
                                    "size": "md",
                                    "weight": "bold"
                                },
                                {
                                    "type": "text",
                                    "text": today_horoscope,
                                    "size": "sm",
                                    "wrap": True,
                                    "offsetTop": "sm"
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "來源：唐綺陽每日星座運勢",
                                            "color": "#bcbcbc",
                                            "size": "xs"
                                        }
                                    ],
                                    "margin": "md",
                                    "spacing": "sm"
                                }
                            ]
                        }
                    ],
                    "spacing": "xl",
                    "paddingAll": "20px"
                }
            ],
            "paddingAll": "0px"
        }
    }
    return FlexSendMessage(alt_text=f'{zodiacSigns_name}{zodiacSigns_date}運勢', contents=contents)
