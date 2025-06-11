class MethodException(Exception):
    def __init__(self, method: str) -> None:
        super().__init__(method)
        self.__method: str = method

    def __str__(self) -> str:
        return f"Method <{self.__method}> does not exist."
