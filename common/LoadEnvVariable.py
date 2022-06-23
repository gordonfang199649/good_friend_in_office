import os

if not os.environ.get('PRODUCTION'):
    from dotenv import load_dotenv

    load_dotenv()

CHANNEL_SECRET = os.getenv('CHANNEL_SECRET')
CHANNEL_ACCESS_TOKEN = os.getenv('CHANNEL_ACCESS_TOKEN')
CAROUSEL_MESSAGE_LIMIT = int(os.getenv('CAROUSEL_MESSAGE_LIMIT'))
BUBBLE_MESSAGE_LIMIT = int(os.getenv('BUBBLE_MESSAGE_LIMIT'))
KKBOX_TOKEN_URL = os.getenv('KKBOX_TOKEN_URL')
KKBOX_CLIENT_ID = os.getenv('KKBOX_CLIENT_ID')
KKBOX_CLIENT_SECRET = os.getenv('KKBOX_CLIENT_SECRET')
KKBOX_WIDGET_URL = os.getenv('KKBOX_WIDGET_URL')
CWB_URL = os.getenv('CWB_URL')
TAIWAN_MEME_API = os.getenv('TAIWAN_MEME_API')
MEME_CONTENT_NUMBER = os.getenv('MEME_CONTENT_NUMBER')
IMAGE_MESSAGE_LIMIT = int(os.getenv('IMAGE_MESSAGE_LIMIT'))
SIGN_ZODIAC_ROOT_URL = os.getenv('SIGN_ZODIAC_ROOT_URL')
SIGN_ZODIAC_URL = os.getenv('SIGN_ZODIAC_URL')
SIGN_ZODIAC_MOOD_THUNDER = os.getenv('SIGN_ZODIAC_MOOD_THUNDER')
SIGN_ZODIAC_MOOD_CLOUDY = os.getenv('SIGN_ZODIAC_MOOD_CLOUDY')
SIGN_ZODIAC_MOOD_RAIN = os.getenv('SIGN_ZODIAC_MOOD_RAIN')
SIGN_ZODIAC_MOOD_PARTLY_CLOUDY = os.getenv('SIGN_ZODIAC_MOOD_PARTLY_CLOUDY')
SIGN_ZODIAC_MOOD_SUNNY = os.getenv('SIGN_ZODIAC_MOOD_SUNNY')
MOTTO_URL = os.getenv('MOTTO_URL')
IMGUR_CLIENT_ID = os.getenv('IMGUR_CLIENT_ID')
IMGUR_CLIENT_SECRET = os.getenv('IMGUR_CLIENT_SECRET')
