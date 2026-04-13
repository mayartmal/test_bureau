UPD Server and Serial Device Test

Serial tests:
Mock mode is a default mode
Use command below to run for real device:
$env:MODE="real"; $env:PORT="COM3"; pytest -v test/