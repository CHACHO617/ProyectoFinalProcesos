from flask import Flask, request, jsonify
import requests
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

SERVICE2_BASE = "http://service2"
SERVICE3_BASE = "http://service3"


# Métrica Prometheus: cuenta de llamadas a /operaciones
operaciones_counter = Counter('operaciones_total', 'Número total de solicitudes a /operaciones')

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/operaciones')
def operaciones():
    operaciones_counter.inc()  # Incrementa la métrica en 1

    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (TypeError, ValueError):
        return jsonify({'error': 'Parámetros inválidos'}), 400

    def safe_request(url):
        try:
            r = requests.get(url)
            return r.json()
        except Exception:
            return {"error": f"Error al conectar con {url}"}

    resultado = {
        'suma': safe_request(f"{SERVICE2_BASE}/suma?a={a}&b={b}").get('resultado'),
        'resta': safe_request(f"{SERVICE2_BASE}/resta?a={a}&b={b}").get('resultado'),
        'multiplicacion': safe_request(f"{SERVICE2_BASE}/multiplicacion?a={a}&b={b}").get('resultado'),
        'division': safe_request(f"{SERVICE3_BASE}/division?a={a}&b={b}").get('resultado'),
        'modulo': safe_request(f"{SERVICE3_BASE}/modulo?a={a}&b={b}").get('resultado'),
    }

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
