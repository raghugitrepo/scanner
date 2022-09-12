import json
from urllib import response
from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

scan_payload = {
    "scanner_name": "Brakeman",
    "language": "Ruby",
    "source_code_url": "https://github.com/manojbinjola/ruby-project"
}


def test_scan():
    response = client.post('/scan', json=scan_payload)
    assert response.status_code == 200


scan_payload_invalid_scanner_name = {
    "scanner_name": "Bandit",
    "language": "Ruby",
    "source_code_url": "https://github.com/manojbinjola/ruby-project"
}


def test_scan_scanner_name_invalid():
    response = client.post('/scan', json=scan_payload_invalid_scanner_name)
    assert response.status_code == 404
    assert response.json() == {'detail': 'Scanner not available'}