from main import app
from unittest.mock import patch
import pytest

client = app.test_client()

class MockResponse:
    def __init__(self, json_data, status_code=200):
        self._json = json_data
        self.status_code = status_code
    def json(self):
        return self._json

@patch('main.requests.get')
def test_operaciones_correctas(mock_get):
    # Simular respuestas secuenciales para suma, resta, multiplicación, división, módulo
    mock_get.side_effect = [
        MockResponse({'resultado': 13}),  # suma
        MockResponse({'resultado': 7}),   # resta
        MockResponse({'resultado': 30}),  # multiplicación
        MockResponse({'resultado': 3.33}),# división
        MockResponse({'resultado': 1})    # módulo
    ]

    response = client.get('/operaciones?a=10&b=3')
    assert response.status_code == 200
    data = response.get_json()
    assert data == {
        'suma': 13,
        'resta': 7,
        'multiplicacion': 30,
        'division': 3.33,
        'modulo': 1
    }

@patch('main.requests.get')
def test_operaciones_integradas(mock_get):
    def fake_response(url):
        if 'suma' in url:
            return MockResponse({'resultado': 15})
        elif 'resta' in url:
            return MockResponse({'resultado': 5})
        elif 'multiplicacion' in url:
            return MockResponse({'resultado': 50})
        elif 'division' in url:
            return MockResponse({'resultado': 2})
        elif 'modulo' in url:
            return MockResponse({'resultado': 0})
        return MockResponse({'error': 'URL inválida'})

    mock_get.side_effect = fake_response

    response = client.get('/operaciones?a=10&b=5')
    assert response.status_code == 200
    data = response.get_json()
    assert data['suma'] == 15
    assert data['resta'] == 5
    assert data['multiplicacion'] == 50
    assert data['division'] == 2
    assert data['modulo'] == 0

def test_parametros_invalidos():
    response = client.get('/operaciones?a=abc&b=5')
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Parámetros inválidos'}
