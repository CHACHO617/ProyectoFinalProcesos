from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SERVICE2_BASE = "http://127.0.0.1:8082"
SERVICE3_BASE = "http://127.0.0.1:8083"

@app.route('/operaciones')
def operaciones():
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
        'division': safe_request(f"{SERVICE3_BASE}/division?a={a}&b={b}").get('resultado', 'error'),
        'modulo': safe_request(f"{SERVICE3_BASE}/modulo?a={a}&b={b}").get('resultado', 'error'),
    }

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

## TEST 123