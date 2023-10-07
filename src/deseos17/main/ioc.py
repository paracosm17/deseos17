from contextlib import contextmanager

from deseos17.adapters.auth.telegram import TelegramAuthenticator
from deseos17.adapters.database.fake_db import FakeGateway
from deseos17.application.auth.use_case import Authenticate
from deseos17.application.create_wish import CreateWish
from deseos17.application.view_wishlist import ViewWishList
from deseos17.domain.services.access import AccessService
from deseos17.domain.services.wish import WishService
from deseos17.presentation.interactor_factory import InteractorFactory


class IoC(InteractorFactory):
    def __init__(self, tg_token: str):
        self.db_gateway = FakeGateway()
        self.tg_token = tg_token

    @contextmanager
    def authenticate(self) -> Authenticate:
        yield Authenticate(
            authenticator=TelegramAuthenticator(self.tg_token),
        )

    @contextmanager
    def view_wishlist(self) -> ViewWishList:
        yield ViewWishList(
            db_gateway=self.db_gateway,
            access_service=AccessService(),
            wish_service=WishService(),
        )

    @contextmanager
    def create_wish(self) -> CreateWish:
        yield CreateWish(
            db_gateway=self.db_gateway,
            access_service=AccessService(),
            wish_service=WishService(),
        )
