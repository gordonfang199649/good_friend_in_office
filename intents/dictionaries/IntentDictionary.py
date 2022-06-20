import re

patterns = {
    re.compile('^[雷達|天氣].*'): ['actions.ActionWeatherInfo', 'get_cloud_image'],
    re.compile('.*[搜尋|搜|找|點播]歌手(.*)'): ['actions.ActionSearchSongsInKKBox', 'search_singer'],
    re.compile('.*[搜尋|搜|找](.*)的專輯'): ['actions.ActionSearchSongsInKKBox', 'search_singer_album'],
    re.compile('.*[搜尋|搜|找](.*)的[歌曲|歌]'): ['actions.ActionSearchSongsInKKBox', 'search_singer_song']
}
