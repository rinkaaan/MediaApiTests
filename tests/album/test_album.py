from openapi_client.models.add_album_in import AddAlbumIn
from tests.clients import fake, albumApi


class Test:
    def test_add_albums(self):
        for i in range(50):
            albumApi.album_post(add_album_in=AddAlbumIn(name=fake.name()))
        # albumApi.album_post(add_album_in=AddAlbumIn(name=fake.name()))
