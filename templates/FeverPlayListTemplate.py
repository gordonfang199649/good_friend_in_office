from linebot.models import (
    FlexSendMessage
)

from templates.KKBoxWidget import KKBoxWidget, WidgetType, Territory, Language, AutoPlay, LOOP

"""
    產製發燒流行播放清單模板
"""

def fever_playlist_template(search_result: list) -> FlexSendMessage:
    contents = dict()
    contents['type'] = 'carousel'
    bubbles = []
    for playlist in search_result:
        # 產生 KKBOX HTML Widgets URL
        widget = KKBoxWidget()
        widget.type = WidgetType.PLAYLIST
        widget.territory = Territory.TAIWAN
        widget.language = Language.TRADITIONAL_CHINESE
        widget.autoplay = AutoPlay.TRUE
        widget.loop = LOOP.TRUE
        widget_url = widget.url(playlist['id'])
        del widget

        bubbles.append({
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": playlist['images'][2]['url'],
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "2:3",
                        "gravity": "top"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": playlist['description'],
                                        "size": "xl",
                                        "color": "#ffffff",
                                        "weight": "bold"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": playlist['owner']['description'] if playlist['owner'][
                                            'description'] else playlist['title'],
                                        "color": "#ebebeb",
                                        "size": "sm",
                                        "flex": 0,
                                        "wrap": True
                                    }
                                ],
                                "spacing": "lg"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "filler"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "filler"
                                            },
                                            {
                                                "type": "text",
                                                "text": "聆聽播放清單",
                                                "color": "#ffffff",
                                                "flex": 0,
                                                "offsetTop": "-2px"
                                            },
                                            {
                                                "type": "filler"
                                            }
                                        ],
                                        "spacing": "sm"
                                    },
                                    {
                                        "type": "filler"
                                    }
                                ],
                                "borderWidth": "1px",
                                "cornerRadius": "4px",
                                "spacing": "sm",
                                "borderColor": "#ffffff",
                                "margin": "xxl",
                                "height": "40px",
                                "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": widget_url
                                }
                            }
                        ],
                        "position": "absolute",
                        "offsetBottom": "0px",
                        "offsetStart": "0px",
                        "offsetEnd": "0px",
                        "backgroundColor": "#03303Acc",
                        "paddingAll": "20px",
                        "paddingTop": "18px"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": playlist['title'][:2],
                                "color": "#ffffff",
                                "align": "center",
                                "offsetTop": "3px"
                            }
                        ],
                        "position": "absolute",
                        "cornerRadius": "20px",
                        "offsetTop": "18px",
                        "backgroundColor": "#ff334b",
                        "offsetStart": "18px",
                        "height": "25px",
                        "width": "53px"
                    }
                ],
                "paddingAll": "0px"
            }
        })
    contents['contents'] = bubbles
    return FlexSendMessage(alt_text=f'發燒流行音樂', contents=contents)
