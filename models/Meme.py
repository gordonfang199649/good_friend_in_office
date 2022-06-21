from common.LoadEnvVariable import TAIWAN_MEME_API

class Meme:
    def __init__(self):
        self.url_prefix = TAIWAN_MEME_API
        self._id = None
        self._url = None
        self._author = None
        self._title = None
        self._pageview = None
        self._total_like_count = None
        self._hashtag = None
        self._contest = None

    """
        :return id
    """

    @property
    def id(self) -> str:
        return self._id

    """
        :param id
    """

    @id.setter
    def id(self, new_id: str):
        self._id = new_id

    """
        :return url
    """

    @property
    def url(self) -> str:
        return self._url

    """
        :param url
    """

    @url.setter
    def url(self, new_url: str):
        self._url = new_url

    """
        :return author
    """

    @property
    def author(self) -> str:
        return self._author

    """
        :param author
    """

    @author.setter
    def author(self, new_author: str):
        self._author = new_author

    """
        :return title
    """

    @property
    def title(self) -> str:
        return self._title

    """
        :param title
    """

    @title.setter
    def title(self, new_autoplay: str):
        self._title = new_autoplay

    """
        :return pageview
    """

    @property
    def pageview(self) -> str:
        return self._pageview

    """
        :param pageview
    """

    @pageview.setter
    def pageview(self, new_pageview: str):
        self._pageview = new_pageview

    """
            :return _total_like_count
        """

    @property
    def total_like_count(self) -> str:
        return self._total_like_count

    """
        :param _total_like_count
    """

    @total_like_count.setter
    def total_like_count(self, new_total_like_count: str):
        self._total_like_count = new_total_like_count

    """
        :param hashtag
    """

    @property
    def hashtag(self) -> str:
        return self._hashtag

    """
        :param hashtag
    """

    @hashtag.setter
    def hashtag(self, new_hashtag: str):
        self._hashtag = new_hashtag

    """
        :param contest
    """

    @property
    def contest(self) -> str:
        return self._contest

    """
        :param contest
    """

    @contest.setter
    def contest(self, new_contest: str):
        self._contest = new_contest

    def api(self):
        url = f'{self.url_prefix}'
        if self.id is not None:
            url = f'{url}&id={self.id}'

        if self.url is not None:
            url = f'{url}&url={self.url}'

        if self.author is not None:
            url = f'{url}&author={self.author}'

        if self.title is not None:
            url = f'{url}&title={self.title}'

        if self.pageview is not None:
            url = f'{url}&pageview={self.pageview}'

        if self.total_like_count is not None:
            url = f'{url}&total_like_count={self.total_like_count}'

        if self.hashtag is not None:
            url = f'{url}&hashtag={self.hashtag}'

        if self.contest is not None:
            url = f'{url}&contest={self.contest}'

        return url
