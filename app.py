from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Variable temporal para guardar el último cálculo
ultimo_resultado = {}

@app.route('/promedio', methods=['POST'])
def calcular_promedio():
    global ultimo_resultado
    datos = request.get_json()
    nombre = datos.get('nombre')
    calificaciones = datos.get('calificaciones', [])
    
    if not calificaciones:
        return jsonify({'error': 'No se proporcionaron calificaciones'}), 400
    
    promedio = sum(calificaciones) / len(calificaciones)
    
    ultimo_resultado = {
        'nombre': nombre,
        'promedio': promedio
    }
    return jsonify(ultimo_resultado)

@app.route('/ver-resultado', methods=['GET'])
def ver_resultado():
    # Retorna un HTML simple para el navegador
    return render_template_string('''
        <h1>Último Promedio Calculado</h1>
        <p><strong>Nombre:</strong> {{ datos.nombre }}</p>
        <p><strong>Promedio:</strong> {{ datos.promedio }}</p>
    ''', datos=ultimo_resultado)

if __name__ == '__main__':
    app.run(debug=True)