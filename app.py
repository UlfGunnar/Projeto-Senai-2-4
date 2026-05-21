from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('Login.html')

@app.route('/login', methods=['POST'])
def processar_login():
    usuario = request.form.get('usuario_login')
    senha = request.form.get('senha_login')

    return redirect(url_for('login_page'))

@app.route('/registrar')
def register_page():
    return render_template('Register.html')

@app.route('/register', methods=['POST'])
def processar_register():
    nome = request.form.get('nome_register')
    usuario = request.form.get('usuario_register')
    senha = request.form.get('senha_register')

    celular = request.form.get('celular_register')
    email = request.form.get('email_register')

    bairro = request.form.get('bairro_register')
    rua = request.form.get('rua_register')
    numero = request.form.get('numero_register')
    complemento = request.form.get('complemento_register')
    
    return redirect(url_for('register_page'))

@app.route('/menu')
def menu_cliente_page():
    return render_template('Menu_cliente.html')

@app.route('/marcar_consulta')
def marcar_consulta_page():
    return render_template('Marcar_consulta.html')

@app.route('/menu_cliente_marcar_consulta', methods=['POST'])
def processar_menu_cliente_marcar_consulta():
    return redirect(url_for('marcar_consulta_page'))

@app.route('/acompanhar_consulta')
def acompanhar_consulta_page():
    return render_template('Acompanhar_consulta.html')

@app.route('/menu_cliente_acompanhar_consulta', methods=['POST']) 
def processar_menu_cliente_acompanhar_consulta():
    return redirect(url_for('acompanhar_consulta_page'))

if __name__ == '__main__':
    app.run(debug=True)