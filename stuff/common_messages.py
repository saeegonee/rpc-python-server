from packet import Packet


class CommonMessage(object):
    def __init__(self) -> None:
        pass

    def not_exist_method(self, client_id: int) -> Packet:
        return Packet(f'[{client_id},"msg","Method does not exist."]')
