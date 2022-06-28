from models import Message

class UserContext:
    def __init__(self):
        self._user_id = None
        self._message = None
        self._url = None

    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, new_user_id: str):
        self._user_id = new_user_id

    @property
    def message(self) -> Message:
        return self._message

    @message.setter
    def message(self, new_message: Message):
        self._message = new_message
