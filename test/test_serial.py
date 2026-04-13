import os
import pytest
from core.serial_device import SerialDevice

@pytest.fixture()
def serial_device():
    port  = os.getenv("PORT", "COM1")
    dev = SerialDevice(port=port)
    dev.connect()
    yield dev
    dev.disconnect()

def test_get_v(serial_device):
    resp = serial_device.get_v()
    assert resp.startswith("V_")

def test_get_a(serial_device):
    resp = serial_device.get_a()
    assert resp.startswith("A_")

def test_get_s(serial_device):
    resp = serial_device.get_s()
    assert resp.startswith("S_")
