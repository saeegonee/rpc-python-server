class Permission(object):

    def common(self) -> list[str]:
        return ["msg"]

    def extend(self) -> list[str]:
        return ["auth"]
