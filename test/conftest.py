import os
import json
from unittest.mock import patch

import pytest

from core.serial_device import SerialDevice
from core.udp_client import UDPClient


class FakeSerial:
    def __init__(self, *args, **kwargs):
        self.is_open = True
        self.last_command = b""

    def write(self, data: bytes):
        self.last_command = data

    def readline(self) -> bytes:
        if self.last_command == b"GET_V\n": return b"V_12V\n"
        if self.last_command == b"GET_A\n": return b"A_1A\n"
        if self.last_command == b"GET_S\n": return b"S_DSA123\n"
        return b"ERROR\n"

    def close(self):
        self.is_open = False


class FakeUDPClient:
    def __init__(self, *args, **kwargs):
        self.is_open = True
        self.last_payload = ""

    def send(self, payload: str):
        self.last_payload = payload

    def recv(self) -> str:
        data = json.loads(self.last_payload)
        cmd = data.get("cmd")
        if cmd == "GET_V":
            return json.dumps({"cmd": "GET_V", "payload": "V_12V"})
        if cmd == "GET_A":
            return json.dumps({"cmd": "GET_A", "payload": "A_1A"})
        if cmd == "GET_S":
            return json.dumps({"cmd": "GET_S", "payload": "S_DSA123"})

        return json.dumps({"error": "UNKNOWN"})

    def close(self):
        self.is_open = False


@pytest.fixture()
def serial_device():
    mode = os.getenv("MODE", "mock")
    if mode == "mock":
        with patch("core.serial_device.serial.Serial", new=FakeSerial):
            dev = SerialDevice(port="COM1")
            dev.connect()
            yield dev
            dev.disconnect()
    else:
        port = os.getenv("PORT", "COM1")
        dev = SerialDevice(port=port)
        dev.connect()
        yield dev
        dev.disconnect()


@pytest.fixture()
def udp_client():
    mode = os.getenv("MODE", "mock")
    if mode == "mock":
        with patch("core.udp_client.websocket.create_connection", new=FakeUDPClient):
            client = UDPClient(url="ws://localhost:8080")
            client.connect()
            yield client
            client.disconnect()
    else:
        url = os.getenv("WS_URL", "ws://localhost:8080")
        client = UDPClient(url=url)
        client.connect()
        yield client
        client.disconnect()
