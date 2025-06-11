class Message(object):

    def start_server(self) -> str:
        return "<<< Server started >>>"

    def stop_server(self) -> str:
        return "<<< Server stopped >>>"

    def connect(self, idx: int) -> str:
        return f"<{idx}> Client connected."

    def disconnect(self, idx: int, err) -> str:
        return f"<{idx}> {err}. Client disconnected."

    def create_room(self, uuid: str) -> str:
        return f"Create new room <{uuid}>."

    def destroy_room(self, uuid: str) -> str:
        return f"Destroy room <{uuid}>."

    def visit_room(self, uuid: str, idx: int) -> str:
        return f"<{idx}> visit room <{uuid}>."

    def leave_room(self, uuid: str, idx: int) -> str:
        return f"<{idx}> leave room <{uuid}>."

    def send_msg(self, msg: str) -> str:
        return f"Send: {msg}"

    def receive_msg(self, msg: str) -> str:
        return f"Receive: {msg}"

    def method_error(self, method: str, err) -> str:
        return f"<{method}> method. {err}"
