from imgurpython import ImgurClient
from imgurpython.imgur.models.gallery_album import GalleryAlbum
from imgurpython.imgur.models.gallery_image import GalleryImage
from common.LoadEnvVariable import IMGUR_CLIENT_ID, IMGUR_CLIENT_SECRET

"""
    查詢Imgur圖片
    :param query_string: 查詢字串
"""

def search_images_in_gallery(query_string: str) -> list[str]:
    client = ImgurClient(IMGUR_CLIENT_ID, IMGUR_CLIENT_SECRET)
    response = client.gallery_search(q=query_string)

    image_links = []
    for galleryObject in response:
        if isinstance(galleryObject, GalleryAlbum):
            image_links.append(galleryObject.images[0]['link'])
        elif isinstance(galleryObject, GalleryImage):
            image_links.append(galleryObject.link)

    return image_links