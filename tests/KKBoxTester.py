import unittest

from agents.KKBox import get_access_token, search_artists, search_artist_albums, search_artist_tracks, search_tracks, \
    search_albums, search_playlists, get_new_hits, list_charts

"""
    測試 KKBOX API 測試集
"""
class TestKKBoxAPIs(unittest.TestCase):
    """
        測試 KKBOX access token 取得
    """

    def test_access_token(self):
        kkbox_token = get_access_token()
        print(kkbox_token.__dict__)
        self.assertIsNotNone(kkbox_token.access_token)

    """
        測試搜尋歌手名稱
    """

    def test_search_artists(self):
        kkbox_token = get_access_token()
        print(kkbox_token.__dict__)
        artist_name = input()
        test_result = search_artists(token=kkbox_token, artist_name=artist_name)
        print(test_result)
        print(len(test_result))
        self.assertGreater(len(test_result), 0)
        self.assertIn(artist_name, test_result[0]['name'])

    """
        測試搜尋歌手專輯
    """

    def test_search_artist_albums(self):
        kkbox_token = get_access_token()
        print(kkbox_token.__dict__)
        artist_name = input()
        test_result = search_artist_albums(token=kkbox_token, artist_name=artist_name)
        print(test_result)
        self.assertGreater(len(test_result), 0)

    """
        測試搜尋歌手歌曲
    """

    def test_search_artist_tracks(self):
        kkbox_token = get_access_token()
        print(kkbox_token.__dict__)
        artist_name = input()
        test_result = search_artist_tracks(token=kkbox_token, keyword=artist_name)
        print(test_result)
        self.assertGreater(len(test_result), 0)

    """
        測試搜尋歌曲
    """

    def test_search_tracks(self):
        kkbox_token = get_access_token()
        print(kkbox_token.__dict__)
        track_name = input()
        test_result = search_tracks(token=kkbox_token, track_name=track_name)
        print(test_result)
        self.assertGreater(len(test_result), 0)
        self.assertIn(track_name, test_result[0]['name'])

    """
        測試搜尋專輯
    """

    def test_search_album(self):
        kkbox_token = get_access_token()
        print(kkbox_token.__dict__)
        album_keyword = input()
        test_result = search_albums(token=kkbox_token, album_keyword=album_keyword)
        print(test_result)
        self.assertGreater(len(test_result), 0)
        self.assertIn(album_keyword, test_result[0]['name'])

    """
        測試搜尋專輯
    """

    def test_search_playlists(self):
        kkbox_token = get_access_token()
        print(kkbox_token.__dict__)
        playlist_keyword = input()
        test_result = search_playlists(token=kkbox_token, playlist_keyword=playlist_keyword)
        print(test_result)
        self.assertGreater(len(test_result), 0)
        self.assertIn(playlist_keyword, test_result[0]['title'])

    """
       測試流行音樂新聞
   """

    def test_get_new_hits(self):
        kkbox_token = get_access_token()
        print(kkbox_token.__dict__)
        test_result = get_new_hits(token=kkbox_token)
        print(test_result)
        self.assertGreater(len(test_result), 0)

    """
        熱門歌曲
        :param token : API access token
        :return 熱門歌曲
    """

    def test_list_charts(self):
        kkbox_token = get_access_token()
        print(kkbox_token.__dict__)
        test_result = list_charts(token=kkbox_token)
        print(test_result)
        self.assertGreater(len(test_result), 0)

if __name__ == '__main__':
    unittest.main()
