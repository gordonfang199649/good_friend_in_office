import random
import re
import requests
from linebot.models import ImageSendMessage, TextSendMessage
import config.Logger
import logging as LOGGER
from common.LoadEnvVariable import MEME_CONTENT_NUMBER
from models.Meme import Meme

"""
    LOGGER
"""

LOGGER.getLogger(__name__)

"""
    全域變數
"""

"""
    抽梗圖
    :param str: 原始訊息
    :param pattern: 正規表達式
    :return Line 訊息封裝物件
"""

def get_meme_picture(intent: str, pattern: re) -> ImageSendMessage or TextSendMessage:
    meme = Meme()
    try_times = 0
    search_result = []

    while try_times < 5 and len(search_result) < 1:
        meme.contest = random.randint(1, int(MEME_CONTENT_NUMBER))
        search_result = requests.get(meme.api()).json()
        try_times = try_times + 1

    if try_times > 5:
        return TextSendMessage(text='沒抽到梗圖，要不要再試試看。')

    # 資料過濾，找出可能比較好笑的梗圖
    # 計算梗圖平均瀏覽次數
    page_views = list(map(lambda data: int(data['pageview']), search_result))
    average_page_views = sum(page_views) / len(search_result)
    search_result = list(filter(lambda data: int(data['pageview']) >= average_page_views, search_result))

    # 計算梗圖平均按讚數
    total_like_count = list(map(lambda data: int(data['total_like_count']), search_result))
    average_total_like_count = sum(total_like_count) / len(search_result)

    # 過濾後的平均按讚數都大於 0，再用留下大於平均按讚數的資料
    if average_total_like_count > 0:
        search_result = list(
            filter(lambda data: int(data['total_like_count']) >= average_total_like_count, search_result))

    # 為避免每次同一主題都抽同一張圖片，將資料打散，隨機抽一張圖片
    random.shuffle(search_result)

    return ImageSendMessage(
        original_content_url=search_result[0]['src'],
        preview_image_url=search_result[0]['src'])

"""
    TODO 抽更多梗圖
    :param str: 原始訊息
    :param pattern: 正規表達式
    :return Line 訊息封裝物件
"""
def get_more_meme_picture(intent: str, pattern: re) -> ImageSendMessage:
    pass
