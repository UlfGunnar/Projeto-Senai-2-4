from flask import Flask, render_template, request, redirect, url_for
from DAO.classes import Cliente, funcionario, Animal, cargo, Consulta, Tipo_de_consulta, Login, Historico
import backend.tratamento_dados as tratar_dados
import re
from datetime import datetime
from DAO.Cliente_dao import ClienteDAO
from DAO.Funcionarios_dao import FuncionarioDAO
from DAO.Animal_dao import AnimalDAO
from DAO.Consulta_dao import ConsultaDAO
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

@app.route('/register', methods=['POST']) #testando
def processar_register():
    nome        = request.form.get('nome_register') 
    cpf         = request.form.get('cpf_register')
    senha       = request.form.get('senha_register')

    celular     = request.form.get('celular_register')
    email       = request.form.get('email_register')

    bairro      = request.form.get('bairro_register') or None
    rua         = request.form.get('rua_register') or None
    numero      = request.form.get('numero_register') or None
    complemento = request.form.get('complemento_register') or None
    
    cpf = cpf.strip().replace(".", "").replace("-", "")
    celular = re.sub(r"\D", "", celular)

    cpf_valido     = tratar_dados.validar_cpf(cpf)
    senha_valida   = tratar_dados.validar_senha(senha)
    nome_valido    = tratar_dados.validar_nome(nome)
    celular_valido = tratar_dados.validar_celular(celular)
    email_valido   = tratar_dados.validar_email(email)
    
    novo_login = Login(
            id_login=None,            
            fk_funcionario=None,       
            senha=senha,               
            fk_cpf=cpf,                
            fk_cargo=None
    )
    if cpf_valido and senha_valida and nome_valido and celular_valido and email_valido:
        novo_cliente = Cliente(
            cpf=cpf,
            nome_cliente=nome,
            celular=celular,
            email=email,
            bairro=bairro,
            rua=rua,
            numero=numero,
            complemento=complemento
        )

        dao = ClienteDAO()
        dao.inserir_cliente(novo_cliente)

        return redirect(url_for('login_page'))

    return redirect(url_for('register_page'))

    
#---------------------------------------#
#---------REGISTRAR FUNCIONÁRIO---------#
#---------------------------------------#

@app.route('/registrar_funcionario')
def register_func_page():
    return render_template('Register_funcionario.html')

@app.route('/register_func', methods=['POST'])
def processar_register_func():
    nome        = request.form.get('nome_register')
    cpf         = request.form.get('cpf_register')
    senha       = request.form.get('senha_register')
    data_nasc   = request.form.get('nasc_register')
    cargo       = request.form.get('cargo_register') 

    celular     = request.form.get('celular_register')
    email       = request.form.get('email_register')

    bairro      = request.form.get('bairro_register')
    rua         = request.form.get('rua_register')
    complemento = request.form.get('complemento_register')

    nome_valido = tratar_dados.validar_nome(nome)
    cpf_valido = tratar_dados.validar_cpf(cpf)
    senha_valida = tratar_dados.validar_senha(senha)
    
    try:
        data_br = datetime.strptime(data_nasc, "%Y-%m-%d").strftime("%d/%m/%Y")
        data_nasc_valida = tratar_dados.validar_data(data_br)
    except (ValueError, TypeError):
        data_nasc_valida = False
        
    cargo_valido = cargo in ['1', '2']
    celular_valido = tratar_dados.validar_celular(celular)
    
    retorno_email = tratar_dados.validar_email(email)
    email_valido = retorno_email[0] if isinstance(retorno_email, tuple) else False
    email_limpo = retorno_email[1] if isinstance(retorno_email, tuple) else email
    
    bairro_valido = tratar_dados.validar_bairro(bairro)
    rua_valida = tratar_dados.validar_rua(rua)
    
    complemento_valido = tratar_dados.validar_complemento(complemento) if complemento else True
    
    if (nome_valido and cpf_valido and senha_valida and data_nasc_valida and 
        cargo_valido and celular_valido and email_valido and 
        bairro_valido and rua_valida and complemento_valido):
        
        novo_funcionario = funcionario(
            None,
            int(cargo),
            nome,
            celular,
            email_limpo,
            bairro,
            rua,
            complemento,
            data_nasc_valida
        )

        dao = FuncionarioDAO()
        dao.salvar_dados(novo_funcionario)
        
        return redirect(url_for('login_page'))
    else:
        return redirect(url_for('register_func_page'))
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

#----------------------------------#
#---------MENU FUNCIONÁRIO---------#
#----------------------------------#

@app.route('/menu_funcionario')
def menu_funcionario_page():
    return render_template('Menu_funcionario.html')

@app.route('/menu_fucionario_gerenciar_consulta', methods=['GET'])
def processar_menu_funcionario_gerenciar_consulta():
    return redirect(url_for('gerenciar_consulta_page'))

#-------------------------------------#
#---------GERENCIAR CONSULTAS---------#
#-------------------------------------#

@app.route('/Gerenciar_consulta')
def gerenciar_consulta_page():
    return render_template('Gerenciar_consulta.html')

@app.route('/concluir_consulta', methods=['POST'])
def processar_concluir_consulta():
    print('botão clicado')
    return redirect(url_for('gerenciar_consulta_page'))

@app.route('/deletar_consulta', methods=['POST'])
def processar_deletar_consulta():
    print('botão clicado')
    return redirect(url_for('gerenciar_consulta_page'))

#---------------------------------#
#---------MARCAR CONSULTA---------#
#---------------------------------#

@app.route('/marcar_consulta')
def marcar_consulta_page():
    return render_template('Marcar_consulta.html')

@app.route('/Voltar', methods=['GET'])
def processar_voltar_menu_cliente():
    return redirect(url_for('menu_cliente_page'))

@app.route('/agendar', methods=['POST']) #funcionando 
def processar_marcar_consulta():    
    tipo_consulta   = request.form.get('select_tipo_consulta')
    especie_animal  = request.form.get('select_especie')
    outro_especie   = request.form.get('outro_animal')
    nome_animal     = request.form.get('nome_animal')
    data_consulta   = request.form.get('form_data')
    hora_consulta   = request.form.get('horario')
    
    bairro          = request.form.get('bairro_register')
    rua             = request.form.get('rua_register')
    numero          = request.form.get('numero_register')
    complemento     = request.form.get('complemento_register')
    proprio_end     = request.form.get('endereco')

    tipo_valido = bool(tipo_consulta)
    nome_valido = tratar_dados.validar_nome.validar_nome(nome_animal)
    data_valida = tratar_dados.validar_data(data_consulta)
    hora_valida = tratar_dados.validar_horario(hora_consulta)

    if especie_animal == "0":
        especie_valida = tratar_dados.validar_outra_especie_animal(outro_especie)
        especie_final  = outro_especie
    else:
        especie_valida = bool(especie_animal)
        especie_final  = especie_animal

    if proprio_end:
        bairro_valido      = True
        rua_valida         = True
        numero_valido      = True
        complemento_valido = True
    else:
        bairro_valido      = tratar_dados.validar_bairro(bairro)
        rua_valida         = tratar_dados.validar_rua(rua)
        numero_valido      = tratar_dados.validar_numero(numero)
        
        if complemento:
            complemento_valido = tratar_dados.complemento_consulta(complemento)
        else:
            complemento_valido = True
            
    if (tipo_valido and especie_valida and nome_valido and data_valida and 
        hora_valida and bairro_valido and rua_valida and numero_valido and complemento_valido):
        
        cpf_cliente = "12345678901" #Provisório

        novo_animal = Animal(
            id_animal   = None,
            fk_cpf      = cpf_cliente,
            nome_animal = nome_animal,
            raca        = None,          
            especie     = especie_final,
            genero      = "N",            
            peso        = 0.0             
        )

        dao = AnimalDAO()
        dao.salvar_dados(novo_animal)


        nova_consulta = Consulta(
            id_consulta         = None,
            fk_animal           = None,  
            fk_cpf              = cpf_cliente,
            fk_matricula_medico = 1,
            fk_tipo_consulta    = int(tipo_consulta),
            dt_consulta         = data_valida,
            hr_consulta         = hora_valida
        )

        dao = ClienteDAO()
        dao.salvar_dados(nova_consulta)
        
        return redirect(url_for('menu_cliente_page'))
    
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