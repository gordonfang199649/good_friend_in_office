class Message:
    def __init__(self):
        self._original_message = None
        self._timestamp = None
        self._domain = None
        self._intent = None

    @property
    def original_message(self) -> str:
        return self._original_message

    @original_message.setter
    def original_message(self, new_original_message: str):
        self._original_message = new_original_message

    @property
    def timestamp(self) -> str:
        return self._timestamp

    @timestamp.setter
    def timestamp(self, new_timestamp: str):
        self._timestamp = new_timestamp

    @property
    def domain(self) -> str:
        return self._domain

    @domain.setter
    def domain(self, new_domain: str):
        self._domain = new_domain

    @property
    def intent(self) -> str:
        return self._intent

    @intent.setter
    def intent(self, new_intent: str):
        self._intent = new_intent
