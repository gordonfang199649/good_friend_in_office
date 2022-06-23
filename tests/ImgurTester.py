import unittest

from imgurpython.imgur.models.gallery_album import GalleryAlbum
from imgurpython.imgur.models.gallery_image import GalleryImage

from common.LoadEnvVariable import IMGUR_CLIENT_ID, IMGUR_CLIENT_SECRET

class TestImgurAPIs(unittest.TestCase):

    def test_search_by_keyword(self):
        from imgurpython import ImgurClient
        client = ImgurClient(IMGUR_CLIENT_ID, IMGUR_CLIENT_SECRET)
        response = client.gallery_search(q="title: spy family")
        for galleryObject in response:
            if isinstance(galleryObject, GalleryAlbum):
                print(galleryObject.images[0]['link'])
            elif isinstance(galleryObject, GalleryImage):
                print(galleryObject.link)
            print(galleryObject.__dict__)

if __name__ == '__main__':
    unittest.main()
