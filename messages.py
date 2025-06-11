class Message(object):

    def start_server(self, addr: str, port: int) -> str:
        return f"<<< Server started {addr}:{port} >>>"

    def stop_server(self) -> str:
        return "<<< Server stopped >>>"

    def connect(self, idx: int) -> str:
        return f"<{idx}> Client connected."

    def disconnect(self, idx: int, err) -> str:
        return f"<{idx}> {err}. Client disconnected."

    def send_msg(self, msg: str) -> str:
        return f"Send: {msg}"

    def receive_msg(self, msg: str) -> str:
        return f"Receive: {msg}"
