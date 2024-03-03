from ksuid import Ksuid

from models.base import MediaModel
from tests.clients import mediaApi, session


class Test:
    def test_add_ksuid(self):
        medias = session.query(MediaModel).all()

        for media in medias:
            media.created_at_ksuid = str(Ksuid(media.created_at))
            # media = session.query(MediaModel).filter(MediaModel.id == media.id).first()
            # media.created_at_ksuid = Ksuid(media.created_at)

        session.commit()
