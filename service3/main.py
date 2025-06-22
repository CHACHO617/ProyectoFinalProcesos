from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/division')
def division():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (TypeError, ValueError):
        return jsonify({'error': 'Parámetros inválidos'}), 400

    if b == 0:
        return jsonify({'error': 'División por cero'}), 400
    return jsonify({'resultado': a / b})

@app.route('/modulo')
def modulo():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (TypeError, ValueError):
        return jsonify({'error': 'Parámetros inválidos'}), 400

    if b == 0:
        return jsonify({'error': 'Módulo por cero'}), 400
    return jsonify({'resultado': a % b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083)
#