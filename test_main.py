from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

def test_get_time():
    with patch("main.get_chile_time") as mock_time:
        mock_time.return_value = {
            "hora": "21:30:46",
            "fecha": "MARZO 31, 2026",
            "dia": "MARTES"
        }
        response = client.get("/time")
        assert response.status_code == 200
        data = response.json()
        assert "hora" in data
        assert "fecha" in data
        assert "dia" in data