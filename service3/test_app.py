from main import app

client = app.test_client()

def test_division_valida():
    response = client.get('/division?a=10&b=2')
    assert response.status_code == 200
    assert response.get_json()['resultado'] == 5.0

def test_division_por_cero():
    response = client.get('/division?a=10&b=0')
    assert response.status_code == 400
    assert response.get_json()['error'] == 'División por cero'

def test_modulo_valido():
    response = client.get('/modulo?a=10&b=3')
    assert response.status_code == 200
    assert response.get_json()['resultado'] == 1.0

def test_modulo_por_cero():
    response = client.get('/modulo?a=10&b=0')
    assert response.status_code == 400
    assert response.get_json()['error'] == 'Módulo por cero'

def test_parametros_invalidos():
    response = client.get('/division?a=hola&b=2')
    assert response.status_code == 400
    assert response.get_json()['error'] == 'Parámetros inválidos'
