import random
import re
from linebot.models import ImageSendMessage
from agents.Imgur import search_images_in_gallery

"""
    傳送間諜家族在Imgur的圖片
    :param str: 原始訊息
    :param pattern: 正規表達式
    :return Line 訊息封裝物件
"""

def send_spy_family_images(intent: str, pattern: re):
    image_links = search_images_in_gallery('title: spy family')
    random.shuffle(image_links)
    return ImageSendMessage(original_content_url=image_links[0], preview_image_url=image_links[0])
