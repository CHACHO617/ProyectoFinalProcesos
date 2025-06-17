from main import app

client = app.test_client()

def test_suma():
    response = client.get('/suma?a=10&b=5')
    assert response.status_code == 200
    assert response.get_json()['resultado'] == 15.0

def test_resta():
    response = client.get('/resta?a=10&b=5')
    assert response.status_code == 200
    assert response.get_json()['resultado'] == 5.0

def test_multiplicacion():
    response = client.get('/multiplicacion?a=10&b=5')
    assert response.status_code == 200
    assert response.get_json()['resultado'] == 50.0

def test_parametros_invalidos_suma():
    response = client.get('/suma?a=hola&b=5')
    assert response.status_code == 400
    assert 'error' in response.get_json()

def test_parametros_faltantes_resta():
    response = client.get('/resta?a=10')  # Falta b
    assert response.status_code == 400
    assert 'error' in response.get_json()
