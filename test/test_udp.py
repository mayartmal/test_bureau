class TestUDPClient:

    def test_get_v(self, udp_client):
        resp = udp_client.get_v()
        assert resp.get("cmd") == "GET_V"
        assert resp.get("payload").startswith("V_")

    def test_get_a(self, udp_client):
        resp = udp_client.get_a()
        assert resp.get("cmd") == "GET_A"
        assert resp.get("payload").startswith("A_")

    def test_get_s(self, udp_client):
        resp = udp_client.get_s()
        assert resp.get("cmd") == "GET_S"
        assert resp.get("payload").startswith("S_")
