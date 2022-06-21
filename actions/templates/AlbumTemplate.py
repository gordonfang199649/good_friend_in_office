from linebot.models import (
    FlexSendMessage
)

from actions.templates.KKBoxWidget import KKBoxWidget, WidgetType, Territory, Language, AutoPlay, LOOP

"""
    產製專輯模板
"""

def album_template(search_result: list) -> FlexSendMessage:
    contents = dict()
    contents['type'] = 'carousel'
    bubbles = []
    artist_name = search_result[0]['artist']['name']
    for album_data in search_result:
        # 產生 KKBOX HTML Widgets URL
        widget = KKBoxWidget()
        widget.type = WidgetType.ALBUM
        widget.territory = Territory.TAIWAN
        widget.language = Language.TRADITIONAL_CHINESE
        widget.autoplay = AutoPlay.TRUE
        widget.loop = LOOP.TRUE
        widget_url = widget.url(album_data['id'])
        del widget

        bubbles.append({
            "type": "bubble",
            "size": "mega",
            "hero": {
                "type": "image",
                "url": album_data['images'][2]['url'],
                "size": "full",
                "align": "center",
                "aspectMode": "cover"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "演唱者：",
                                                "flex": 3,
                                                "size": "lg"
                                            },
                                            {
                                                "type": "text",
                                                "text": album_data['artist']['name'],
                                                "size": "lg",
                                                "weight": "bold",
                                                "flex": 4
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "專輯名稱：",
                                                "flex": 3,
                                                "size": "lg"
                                            },
                                            {
                                                "type": "text",
                                                "text": album_data['name'],
                                                "flex": 4,
                                                "size": "lg"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "發行日：",
                                                "flex": 3,
                                                "size": "lg"
                                            },
                                            {
                                                "type": "text",
                                                "text": album_data['release_date'],
                                                "size": "lg",
                                                "flex": 4
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "專輯簡介：",
                                                "flex": 3,
                                                "size": "lg"
                                            },
                                            {
                                                "type": "text",
                                                "text": 'KKBOX連結',
                                                "size": "lg",
                                                "flex": 4,
                                                "action": {
                                                    "type": "uri",
                                                    "label": "專輯簡介",
                                                    "uri": album_data['url']
                                                },
                                            }
                                        ]
                                    }
                                ],
                                "spacing": "sm"
                            }
                        ],
                        "paddingAll": "20px"
                    }
                ],
                "paddingAll": "0px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "uri",
                            "label": "聆聽專輯",
                            "uri": widget_url
                        },
                        "style": "primary",
                        "offsetBottom": "md"
                    }
                ]
            }
        })
    contents['contents'] = bubbles
    return FlexSendMessage(alt_text=f'歌手{artist_name}專輯', contents=contents)
