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

def test_response_es_json():
    with patch("main.get_chile_time") as mock_time:
        mock_time.return_value = {
            "hora": "21:30:46",
            "fecha": "MARZO 31, 2026",
            "dia": "MARTES"
        }
        response = client.get("/time")
        assert response.headers["content-type"] == "application/json"

def test_hora_formato_correcto():
    with patch("main.get_chile_time") as mock_time:
        mock_time.return_value = {
            "hora": "21:30:46",
            "fecha": "MARZO 31, 2026",
            "dia": "MARTES"
        }
        response = client.get("/time")
        data = response.json()
        hora = data["hora"]
        partes = hora.split(":")
        assert len(partes) == 3  