from linebot.models import (
    FlexSendMessage
)

from templates.KKBoxWidget import KKBoxWidget, WidgetType, Territory, Language, AutoPlay, LOOP

"""
    產製歌曲模板
"""

def track_template(search_result: list) -> FlexSendMessage:
    contents = dict()
    contents['type'] = 'carousel'
    bubbles = []

    artist_name = search_result[0]['album']['artist']['name']
    for track_data in search_result:
        # 產生 KKBOX HTML Widgets URL
        widget = KKBoxWidget()
        widget.type = WidgetType.SONG
        widget.territory = Territory.TAIWAN
        widget.language = Language.TRADITIONAL_CHINESE
        widget.autoplay = AutoPlay.TRUE
        widget.loop = LOOP.TRUE
        widget_url = widget.url(track_data['id'])
        del widget

        bubbles.append({
            "type": "bubble",
            "size": "mega",
            "hero": {
                "type": "image",
                "url": track_data['album']['images'][2]['url'],
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
                                                "text": track_data['album']['artist']['name'],
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
                                                "text": "歌曲名稱：",
                                                "flex": 3,
                                                "size": "lg"
                                            },
                                            {
                                                "type": "text",
                                                "text": track_data['name'],
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
                                                "text": "收錄專輯：",
                                                "flex": 3,
                                                "size": "lg"
                                            },
                                            {
                                                "type": "text",
                                                "text": track_data['album']['name'],
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
                                                "text": "歌曲總長：",
                                                "flex": 3,
                                                "size": "lg"
                                            },
                                            {
                                                "type": "text",
                                                "text": f"{int(track_data['duration']/1000/60)} 分鐘",
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
                                                "text": "歌曲簡介：",
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
                                                    "uri": track_data['url']
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
                            "label": "聆聽單曲",
                            "uri": widget_url
                        },
                        "style": "primary",
                        "offsetBottom": "md"
                    }
                ]
            }
        })
    contents['contents'] = bubbles
    return FlexSendMessage(alt_text=f'歌手{artist_name}歌單', contents=contents)
