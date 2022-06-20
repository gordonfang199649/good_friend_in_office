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
