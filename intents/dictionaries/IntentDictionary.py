import re

patterns = {
    re.compile('^[雷達|天氣].*'): ['actions.ActionWeatherInfo', 'get_cloud_image'],
    re.compile('.*[搜尋|搜|找|點播]歌手(.*)'): ['actions.ActionSearchSongsInKKBox', 'search_singer'],
    re.compile('.*[搜尋|搜|找](.*)的專輯'): ['actions.ActionSearchSongsInKKBox', 'search_singer_album'],
    re.compile('.*[搜尋|搜|找](.*)的[歌曲|歌]'): ['actions.ActionSearchSongsInKKBox', 'search_singer_song'],
    re.compile('.*[搜尋|搜|找]專輯(.*)'): ['actions.ActionSearchSongsInKKBox', 'search_possible_albums'],
    re.compile('.*[搜尋|搜|找][歌曲|歌](.*)'): ['actions.ActionSearchSongsInKKBox', 'search_possible_songs'],
    re.compile('.*流行音樂.*'): ['actions.ActionSearchSongsInKKBox', 'list_fever_playlists'],
    re.compile('.*排行榜.*'): ['actions.ActionSearchSongsInKKBox', 'view_charts'],
    re.compile('.*多.*梗圖.*'): ['actions.ActionMemePictures', 'get_more_meme_picture'],
    re.compile('.*梗圖.*'): ['actions.ActionMemePictures', 'get_meme_picture']
}
