import serial


class SerialDevice:
    def __init__(self, port, rate = 9600, timeout = 10):
        self.port = port
        self.rate = rate
        self.timeout = timeout
        self.conn = None

    def connect(self):
        self.conn = serial.Serial(
            port=self.port,
            baudrate=self.rate,
            timeout=self.timeout
        )

    def disconnect(self):
        if self.conn and self.conn.is_open:
            self.conn.close()

    def _send_cmd(self, cmd) -> str:
        if not self.conn or not self.conn.is_open:
            raise ConnectionError("There is no connection")
        self.conn.write(f"{cmd}\n".encode("utf-8"))
        return self.conn.readLine().decode("utf-8").strip()

    def get_v(self) -> str:
        return self._send_cmd("GET_V")

    def get_a(self) -> str:
        return self._send_cmd("GET_A")

    def get_s(self) -> str:
        return self._send_cmd("GET_S")
