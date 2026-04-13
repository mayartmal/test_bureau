# UDP Server and Serial Device Test

## Serial tests:
* **Mock mode** is a default mode

* Use command below to run for mock device:
pytest -v test/test_serial.py
* Use command below to run for real device:
\$env:MODE="real"; $env:PORT="COM3"; pytest -v test/test_serial.py

## UDP tests:
* **Mock mode** is a default mode
* Use command below to run for mock device:
pytest -v test/test_udp.py
* Use command below to run for real device:
\$env:MODE="real"; WS_URL=ws://localhost:8080; pytest -v test/test_udp.py