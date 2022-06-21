import unittest
from urllib.parse import unquote
import requests

from models.Meme import Meme

class TestMemeAPIs(unittest.TestCase):

    def test_apis(self):
        meme = Meme()
        meme.contest = '11'
        requests.get(meme.api()).json()
        print((requests.get(meme.api()).json()))

if __name__ == '__main__':
    unittest.main()
