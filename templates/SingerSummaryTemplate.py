from linebot.models import (
    MessageAction, CarouselColumn, CarouselTemplate, TemplateSendMessage, URIAction
)

"""
    產製歌手模板
"""

def singer_template(search_result: list) -> TemplateSendMessage:
    content = list()
    for singer_data in search_result:
        content.append(
            CarouselColumn(
                thumbnail_image_url=singer_data['images'][1]['url'],
                title=singer_data['name'],
                text=singer_data['name'],
                actions=[
                    URIAction(
                        label='KKBOX 歌手資訊',
                        uri=singer_data['url']
                    ),
                    MessageAction(
                        label='專輯',
                        text=f"為您搜尋{singer_data['name']}的專輯..."
                    ),
                    MessageAction(
                        label='歌曲',
                        text=f"為您搜尋{singer_data['name']}的歌曲..."
                    )
                ]
            ))

    return TemplateSendMessage(
        alt_text='Singer template',
        template=CarouselTemplate(
            columns=content
        )
    )
