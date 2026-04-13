import json
import websocket


class UDPClient:
    def __init__(self, url: str):
        self.url = url
        self.ws = None

    def connect(self):
        self.ws = websocket.create_connection(self.url)

    def disconnect(self):
        if self.ws:
            self.ws.close()

    def _send_cmd(self, cmd: str) -> dict:
        payload = json.dumps({"cmd": cmd})
        self.ws.send(payload)
        return json.loads(self.ws.recv())

    def get_v(self) -> dict:
        return self._send_cmd("GET_V")

    def get_a(self) -> dict:
        return self._send_cmd("GET_A")

    def get_s(self) -> dict:
        return self._send_cmd("GET_S")