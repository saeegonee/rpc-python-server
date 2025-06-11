class Workshop(object):
    def __init__(self) -> None:
        pass

    async def auth(self) -> None:
        print("Auth working.")

    async def verify(self) -> bool:
        print("Verfy working.")
        return True
