import requests

# URL base da API para testes
BASE_URL = "http://127.0.0.1:8000"

def test_create_reservation():
    """Testa a criação de uma nova reserva."""
    response = requests.post(f"{BASE_URL}/reservations/", json={
        "name": "Test User",
        "hotel_name": "Test Hotel",
        "check_in": "2023-01-01",
        "check_out": "2023-01-02"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"

def test_get_reservations():
    """Testa a listagem de reservas."""
    response = requests.get(f"{BASE_URL}/reservations/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Verifica se o retorno é uma lista
