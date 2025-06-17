from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/suma')
def suma():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (TypeError, ValueError):
        return jsonify({'error': 'Parámetros inválidos'}), 400
    return jsonify({'resultado': a + b})

@app.route('/resta')
def resta():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (TypeError, ValueError):
        return jsonify({'error': 'Parámetros inválidos'}), 400
    return jsonify({'resultado': a - b})

@app.route('/multiplicacion')
def multiplicacion():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (TypeError, ValueError):
        return jsonify({'error': 'Parámetros inválidos'}), 400
    return jsonify({'resultado': a * b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
