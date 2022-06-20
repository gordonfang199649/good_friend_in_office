import logging as LOGGER
from kkbox_developer_sdk.access_token import KKBOXAccessToken
from kkbox_developer_sdk.auth_flow import KKBOXOAuth
from kkbox_developer_sdk.api import KKBOXAPI
from kkbox_developer_sdk.search_fetcher import KKBOXSearchTypes
from kkbox_developer_sdk.territory import KKBOXTerritory

from common.LoadEnvVariable import KKBOX_CLIENT_ID, KKBOX_CLIENT_SECRET

"""
    LOGGER
"""
LOGGER.getLogger(__name__)

"""
Global variables
"""

"""
    取得 API access token
    要打 KKBOX 任一 API 前先要去得 Oauth2.0 的 access token
    :return access token
"""

def get_access_token() -> KKBOXAccessToken:
    auth = KKBOXOAuth(KKBOX_CLIENT_ID, KKBOX_CLIENT_SECRET)
    token = auth.fetch_access_token_by_client_credentials()
    return token

"""
    搜尋歌手
    :param token : API access token
    :param artist_name : 歌手關鍵字
    :return 符合關鍵字的歌手
"""
def search_artists(token: KKBOXAccessToken, artist_name: str):
    kkbox_api = KKBOXAPI(token)

    search_results = kkbox_api.search_fetcher.search(
        artist_name,
        types=[KKBOXSearchTypes.ARTIST],
        terr=KKBOXTerritory.TAIWAN)

    return search_results['artists']['data']

"""
    搜尋歌手專輯
    :param token : API access token
    :param artist_name : 歌手關鍵字
    :return 歌手專輯
"""
def search_artist_albums(token: KKBOXAccessToken, artist_name: str):
    kkbox_api = KKBOXAPI(token)

    search_results = kkbox_api.search_fetcher.search(
        artist_name,
        types=[KKBOXSearchTypes.ARTIST],
        terr=KKBOXTerritory.TAIWAN)

    search_data = search_results['artists']['data']
    if len(search_data) > 0:
        artist_id = search_data[0]['id']
        return kkbox_api.artist_fetcher.fetch_albums_of_artist(artist_id)

    return []

"""
    搜尋歌手歌曲
    :param token : API access token
    :param artist_name : 歌手關鍵字
    :return 歌手歌曲
"""
def search_artist_tracks(token: KKBOXAccessToken, artist_name: str):
    kkbox_api = KKBOXAPI(token)

    search_results = kkbox_api.search_fetcher.search(
        artist_name,
        types=[KKBOXSearchTypes.ARTIST],
        terr=KKBOXTerritory.TAIWAN)

    search_data = search_results['artists']['data']
    if len(search_data) > 0:
        artist_id = search_data[0]['id']
        return kkbox_api.artist_fetcher.fetch_top_tracks_of_artist(artist_id)

    return []

"""
    搜尋 KKBOX 歌曲
    :param token : API access token
    :param track_name : 歌曲關鍵字
    :return 符合關鍵字的歌曲
"""
def search_tracks(token: KKBOXAccessToken, track_name: str):
    kkbox_api = KKBOXAPI(token)

    # 目前只開放搜尋台灣的歌曲
    search_results = kkbox_api.search_fetcher.search(
        track_name,
        types=[KKBOXSearchTypes.TRACK],
        terr=KKBOXTerritory.TAIWAN)

    return search_results['tracks']['data']

"""
    搜尋 KKBOX 歌單
    :param token : API access token
    :param playlist_keyword : 歌單關鍵字
    :return 符合關鍵字的歌單
"""
def search_playlists(token: KKBOXAccessToken, playlist_keyword: str):
    kkbox_api = KKBOXAPI(token)

    # 目前只開放搜尋台灣的歌單
    search_results = kkbox_api.search_fetcher.search(
        playlist_keyword,
        types=[KKBOXSearchTypes.PLAYLIST],
        terr=KKBOXTerritory.TAIWAN)
    return search_results['playlists']['data']

"""
    搜尋 KKBOX 專輯
    :param token : API access token
    :param album_keyword : 專輯關鍵字
    :return 符合關鍵字的專輯
"""
def search_albums(token: KKBOXAccessToken, album_keyword: str):
    kkbox_api = KKBOXAPI(token)

    # 目前只開放搜尋台灣的專輯
    search_results = kkbox_api.search_fetcher.search(
        album_keyword,
        types=[KKBOXSearchTypes.ALBUM],
        terr=KKBOXTerritory.TAIWAN)
    return search_results['albums']['data']

"""
    搜尋流行音樂新聞
    :param token : API access token
    :return 發燒音樂
"""

def get_new_hits(token: KKBOXAccessToken):
    kkbox_api = KKBOXAPI(token)
    return kkbox_api.new_hits_playlist_fetcher.fetch_all_new_hits_playlists(terr=KKBOXTerritory.TAIWAN)['data']

"""
    熱門歌曲
    :param token : API access token
    :return 熱門歌曲
"""

def list_charts(token: KKBOXAccessToken):
    kkbox_api = KKBOXAPI(token)
    return kkbox_api.chart_fetcher.fetch_charts(terr=KKBOXTerritory.TAIWAN)
