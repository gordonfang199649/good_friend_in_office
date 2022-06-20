import logging as LOGGER
import random
import re

from linebot.models import FlexSendMessage, TextSendMessage

from actions.templates.AlbumTemplate import album_template
from actions.templates.SingerSummaryTemplate import singer_template
from actions.templates.SongTemplate import track_template
from agents.KKBox import get_access_token, search_artists, search_artist_albums, search_artist_tracks
from common.LoadEnvVariable import CAROUSEL_MESSAGE_LIMIT, BUBBLE_MESSAGE_LIMIT
from utils.StringUtils import is_substring_ignore_cases

"""
    LOGGER
"""
LOGGER.getLogger(__name__)

"""
    搜尋歌手相關資訊
    :param str: 原始訊息
    :param pattern: 正規表達式
    :return Line 訊息封裝物件
"""

def search_singer(intent: str, pattern: re) -> FlexSendMessage or TextSendMessage:
    # 取出訊息關鍵字
    matched = pattern.match(intent)
    singer_name = matched.group(1)

    # 取得 KKBOX 的 access token
    kkbox_access_token = get_access_token()

    # 搜尋歌手資訊
    search_result = search_artists(token=kkbox_access_token, artist_name=singer_name)

    # 資料過濾
    # 避免出現跟使用搜尋不相關的歌手
    search_result = list(filter(lambda singer: is_substring_ignore_cases(singer_name, singer['name']), search_result))

    if search_result is None or len(search_result) < 1:
        return TextSendMessage(text='很抱歉，搜尋不到您輸入的歌手，要不要換一個試試看。')

    # 卡片標題不得超過 40 字
    for singer_data in search_result:
        singer_data['name'] = singer_data['name'][:40]

    # Carousel樣板 LINE 目前限制只能放 10 個
    if len(search_result) > CAROUSEL_MESSAGE_LIMIT:
        search_result = search_result[:CAROUSEL_MESSAGE_LIMIT]

    return singer_template(search_result)

"""
    搜尋歌手專輯
    :param str: 原始訊息
    :param pattern: 正規表達式
    :return Line 訊息封裝物件
"""

def search_singer_album(intent: str, pattern: re) -> FlexSendMessage or TextSendMessage:
    # 取出訊息關鍵字
    matched = pattern.match(intent)
    singer_name = matched.group(1)

    # 取得 KKBOX 的 access token
    kkbox_access_token = get_access_token()

    # 搜尋歌手資訊
    search_result = search_artist_albums(token=kkbox_access_token, artist_name=singer_name)['data']

    # 資料過濾
    # 避免出現跟使用搜尋跟歌手不相關的專輯
    search_result = list(filter(lambda singer: singer_name in singer['artist']['name'], search_result))

    if search_result is None or len(search_result) < 1:
        return TextSendMessage(text='很抱歉，搜尋不到您輸入的歌手，要不要換一個試試看。')

    # Flex 樣板 LINE 目前限制只能放 12 個 Bubble Message
    if len(search_result) > BUBBLE_MESSAGE_LIMIT:
        # 如果有很多專輯，隨機抽 12 組
        random.shuffle(search_result)
        search_result = search_result[:BUBBLE_MESSAGE_LIMIT]

    return album_template(search_result)

"""
    搜尋歌手歌曲
    :param str: 原始訊息
    :param pattern: 正規表達式
    :return Line 訊息封裝物件
"""

def search_singer_song(intent: str, pattern: re) -> FlexSendMessage or TextSendMessage:
    # 取出訊息關鍵字
    matched = pattern.match(intent)
    singer_name = matched.group(1)

    # 取得 KKBOX 的 access token
    kkbox_access_token = get_access_token()

    # 搜尋歌手資訊
    search_result = search_artist_tracks(token=kkbox_access_token, artist_name=singer_name)['data']

    # 資料過濾
    # 避免出現跟使用搜尋跟歌手不相關的的歌曲
    search_result = list(filter(lambda singer: singer_name in singer['album']['artist']['name'], search_result))

    if search_result is None or len(search_result) < 1:
        return TextSendMessage(text='很抱歉，搜尋不到您輸入的歌手，要不要換一個試試看。')

    # Flex 樣板 LINE 目前限制只能放 12 個 Bubble Message
    if len(search_result) > BUBBLE_MESSAGE_LIMIT:
        # 如果有很多歌曲，隨機抽 12 組
        random.shuffle(search_result)
        search_result = search_result[:BUBBLE_MESSAGE_LIMIT]

    return track_template(search_result)
