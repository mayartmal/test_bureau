class TestSerial:

    def test_get_v(self, serial_device):
        resp = serial_device.get_v()
        assert resp.startswith("V_")

    def test_get_a(self, serial_device):
        resp = serial_device.get_a()
        assert resp.startswith("A_")

    def test_get_s(self, serial_device):
        resp = serial_device.get_s()
        assert resp.startswith("S_")
