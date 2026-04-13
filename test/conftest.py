import os
import pytest
from unittest.mock import patch
from core.serial_device import SerialDevice

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
        port  = os.getenv("PORT", "COM1")
        dev = SerialDevice(port=port)
        dev.connect()
        yield dev
        dev.disconnect()