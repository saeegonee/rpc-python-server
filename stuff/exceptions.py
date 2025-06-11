class MethodException(Exception):
    def __init__(self, method: str, err) -> None:
        super().__init__(method)
        self.__method: str = method
        self.__err = err

    def __str__(self) -> str:
        return f"Try <{self.__method}>. {self.__err}"
