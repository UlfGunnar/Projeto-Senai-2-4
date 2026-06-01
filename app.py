from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#-----------------------#
#---------LOGIN---------#
#-----------------------#

@app.route('/')
def login_page():
    return render_template('Login.html')

@app.route('/login', methods=['POST'])
def processar_login():
    usuario = request.form.get('usuario_login')
    senha = request.form.get('senha_login')

    return redirect(url_for('login_page'))

#---------------------------#
#---------REGISTRAR---------#
#---------------------------#

@app.route('/registrar')
def register_page():
    return render_template('Register.html')

@app.route('/register', methods=['POST'])
def processar_register():
    nome        = request.form.get('nome_register')
    cpf         = request.form.get('cpf_register')
    senha       = request.form.get('senha_register')

    celular     = request.form.get('celular_register')
    email       = request.form.get('email_register')

    bairro      = request.form.get('bairro_register')
    rua         = request.form.get('rua_register')
    numero      = request.form.get('numero_register')
    complemento = request.form.get('complemento_register')
    
    return redirect(url_for('register_page'))

#---------------------------------------#
#---------REGISTRAR FUNCIONÁRIO---------#
#---------------------------------------#

@app.route('/registrar_funcionario')
def register_func_page():
    return render_template('Register_funcionario.html')

#------------------------------#
#---------MENU CLIENTE---------#
#------------------------------#

@app.route('/menu_cliente')
def menu_cliente_page():
    return render_template('Menu_cliente.html')

@app.route('/menu_cliente_marcar_consulta', methods=['GET'])
def processar_menu_cliente_marcar_consulta():
    return redirect(url_for('marcar_consulta_page'))

@app.route('/menu_cliente_acompanhar_consulta', methods=['GET']) 
def processar_menu_cliente_acompanhar_consulta():
    return redirect(url_for('acompanhar_consulta_page'))

@app.route('/verificar_historico', methods=['GET']) 
def processar_menu_cliente_verificar_historico():
    return redirect(url_for('historico_page'))

@app.route('/sair', methods=['GET'])
def sair_login():
    return redirect(url_for('login_page'))

#---------------------------------#
#---------MARCAR CONSULTA---------#
#---------------------------------#

@app.route('/marcar_consulta')
def marcar_consulta_page():
    return render_template('Marcar_consulta.html')

@app.route('/Voltar', methods=['GET'])
def processar_voltar_menu_cliente():
    return redirect(url_for('menu_cliente_page'))

@app.route('/agendar', methods=['POST']) 
def processar_marcar_consulta():    
    tipo_consulta           = request.form.get('select_tipo_consulta')
    especie_animal          = request.form.get('select_especie')
    outro_especie           = request.form.get('outro_animal')
    nome_animal             = request.form.get('nome_animal')

    data_consulta           = request.form.get('form_data')
    hora_consulta           = request.form.get('horario')

    bairro_consulta         = request.form.get('bairro_register')
    rua_consulta            = request.form.get('rua_register')
    num_consulta            = request.form.get('numero_register')
    complemento_consulta    = request.form.get('complemento_register')
    proprio_endereco        = request.form.get('endereco')

    # não tem required nos inputs, pois alguns não aceitam, backend terá que checar se possuiem algum valor 

    return redirect(url_for('marcar_consulta_page'))

#-------------------------------------#
#---------ACOMPANHAR CONSULTA---------#
#-------------------------------------#

@app.route('/acompanhar_consulta')
def acompanhar_consulta_page():
    return render_template('Acompanhar_consulta.html')

#-------------------------------------#
#---------Verificar Histórico---------#
#-------------------------------------#

@app.route('/historico_consulta')
def historico_page():
    return render_template('historico.html')

@app.route('/filtro', methods=['POST'])
def processar_filtro():
    filtro = request.form.get('txt_filtro')

    return redirect(url_for('historico_page'))

#---------------------#
#---------APP---------#
#---------------------#

if __name__ == '__main__':
    app.run(debug=True)