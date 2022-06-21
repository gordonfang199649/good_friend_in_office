from linebot.models import (
    FlexSendMessage
)

from actions.templates.KKBoxWidget import KKBoxWidget, WidgetType, Territory, Language, AutoPlay, LOOP

"""
    產製發燒流行播放清單模板
"""

def chart_template(search_result: list) -> FlexSendMessage:
    contents = dict()
    contents['type'] = 'carousel'
    bubbles = []
    for chart in search_result:
        # 產生 KKBOX HTML Widgets URL
        widget = KKBoxWidget()
        widget.type = WidgetType.PLAYLIST
        widget.territory = Territory.TAIWAN
        widget.language = Language.TRADITIONAL_CHINESE
        widget.autoplay = AutoPlay.TRUE
        widget.loop = LOOP.TRUE
        widget_url = widget.url(chart['id'])
        del widget

        bubbles.append({
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": chart['images'][2]['url'],
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "1:1",
                        "gravity": "center"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "position": "absolute",
                        "background": {
                            "type": "linearGradient",
                            "angle": "0deg",
                            "endColor": "#00000000",
                            "startColor": "#000000FF"
                        },
                        "width": "100%",
                        "height": "40%",
                        "offsetBottom": "0px",
                        "offsetStart": "0px",
                        "offsetEnd": "0px"
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
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": chart['title'],
                                                "size": "xl",
                                                "color": "#ffffff"
                                            }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "color": "#ffffff",
                                                        "size": "md",
                                                        "flex": 0,
                                                        "align": "end",
                                                        "text": f"播放即時{chart['description'][:4]}排行榜"
                                                    }
                                                ],
                                                "flex": 0,
                                                "spacing": "lg"
                                            }
                                        ]
                                    }
                                ],
                                "spacing": "xs",
                                "flex": 3
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": "https://icon-library.com/images/play-icon-white-png/play-icon-white-png-4.jpg",
                                        "size": "full",
                                        "aspectMode": "cover"
                                    }
                                ],
                                "cornerRadius": "100px"
                            }
                        ],
                        "position": "absolute",
                        "offsetBottom": "0px",
                        "offsetStart": "0px",
                        "offsetEnd": "0px",
                        "paddingAll": "20px",
                        "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": widget_url
                        }
                    }
                ],
                "paddingAll": "0px"
            }
        })
    contents['contents'] = bubbles
    return FlexSendMessage(alt_text=f'發燒流行音樂', contents=contents)
