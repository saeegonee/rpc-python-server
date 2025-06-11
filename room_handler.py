from stuff.options import TOKEN


class RoomHandlerCommon(object):

    def _check_token(self, token: str) -> bool:
        if token != TOKEN:
            return False
        return True

    def auth(self, token: str) -> None:
        if self._check_token(token):
            # TODO. Extend room
            pass
        else:
            # TODO. Pity request
            pass

    def ready(self) -> None:
        """Set ready for game."""
