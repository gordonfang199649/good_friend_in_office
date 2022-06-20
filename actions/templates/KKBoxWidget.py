from common.LoadEnvVariable import KKBOX_WIDGET_URL

class WidgetType:
    SONG = 'song'
    ALBUM = 'album'
    PLAYLIST = 'playlist'

class Territory:
    TAIWAN = 'TW'
    HONG_KONG = 'HK'
    SINGAPORE = 'SG'
    MALAYSIA = 'MY'
    JAPAN = 'JP'

class Language:
    TRADITIONAL_CHINESE = 'TC'
    SIMPLIFIED_CHINESE = 'SC'
    JAPANESE = 'JA'
    ENGLISH = 'EN'
    MALAYSIAN = 'MS'

class AutoPlay:
    TRUE = 'true'
    FALSE = 'false'

class LOOP:
    TRUE = 'true'
    FALSE = 'false'

class KKBoxWidget:
    def __init__(self):
        self.url_prefix = KKBOX_WIDGET_URL
        self._type = None
        self._territory = None
        self._language = None
        self._autoplay = None
        self._loop = None

    """
        :return type
    """

    @property
    def type(self) -> str:
        return self._type

    """
        :param type
    """

    @type.setter
    def type(self, new_type: str):
        self._type = new_type

    """
        :return territory
    """

    @property
    def territory(self) -> str:
        return self._territory

    """
        :param territory
    """

    @territory.setter
    def territory(self, new_territory: str):
        self._territory = new_territory

    """
        :return language
    """

    @property
    def language(self) -> str:
        return self._language

    """
        :param language
    """

    @language.setter
    def language(self, new_language: str):
        self._language = new_language

    """
        :return autoplay
    """

    @property
    def autoplay(self) -> str:
        return self._autoplay

    """
        :param autoplay
    """

    @autoplay.setter
    def autoplay(self, new_autoplay: str):
        self._autoplay = new_autoplay

    """
        :return loop
    """

    @property
    def loop(self) -> str:
        return self._loop

    """
        :param loop
    """

    @loop.setter
    def loop(self, new_loop: str):
        self._loop = new_loop

    def url(self, kkbox_id):
        url = f'{self.url_prefix}id={kkbox_id}'
        if self.type is not None:
            url = f'{url}&type={self.type}'

        if self.territory is not None:
            url = f'{url}&terr={self.territory}'

        if self.language is not None:
            url = f'{url}&lang={self.language}'

        if self.autoplay is not None:
            url = f'{url}&lang={self.autoplay}'

        if self.loop is not None:
            url = f'{url}&lang={self.loop}'

        return url
