from actions.ActionZodiacSign import zodiacSigns_convert, ask_users_zodiac_sign, get_today_fortune, \
    reply_users_not_existed_sign
from app import message_cache
from intents.handlers.AbstractHandler import AbstractHandler
from models.UserContext import UserContext

def dispatch(user_context: UserContext):
    zodiac_sign_asking_handler = ZodiacSignAskingHandler()
    # fortune_telling_handler = FortuneTellingHandler()
    # zodiac_sign_asking_handler.set_next(fortune_telling_handler)
    # zodiac_sign_not_exists_handler = ZodiacSignNotExistsHandler()
    # zodiac_sign_asking_handler.set_next(zodiac_sign_not_exists_handler)

    return zodiac_sign_asking_handler.handle(request=user_context)

class ZodiacSignAskingHandler(AbstractHandler):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler: AbstractHandler):
        self._next_handler = handler

    def handle(self, request: UserContext):
        english_zodiac_sign = contains_zodiac_sign(message=request.message.original_message)
        if english_zodiac_sign:
            return get_today_fortune(english_zodiac_sign=english_zodiac_sign)
        # return ask_users_zodiac_sign()

        if self._next_handler is not None:
            return self._next_handler.handle(request=request)

        return None

class FortuneTellingHandler(AbstractHandler):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler: AbstractHandler):
        self._next_handler = handler

    def handle(self, request: UserContext):
        english_zodiac_sign = contains_zodiac_sign(message=request.message.original_message)
        if english_zodiac_sign:
            return get_today_fortune(english_zodiac_sign=english_zodiac_sign)

        if self._next_handler is not None:
            return self._next_handler.handle(request=request)

        return None

class ZodiacSignNotExistsHandler(AbstractHandler):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler: AbstractHandler):
        self._next_handler = handler

    def handle(self, request: UserContext):
        return reply_users_not_existed_sign()

def contains_zodiac_sign(message: str) -> str:
    for pattern, english_name in zodiacSigns_convert.items():
        matched = pattern.match(message)
        if matched:
            return english_name
    return ''
