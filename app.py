from flask import Flask, render_template, request, redirect, url_for, flash
from backend.classes import Cliente, funcionario, Animal, cargo, Consulta, Tipo_de_consulta, Login, Historico
import backend.tratamento_dados as tratar_dados
from datetime import datetime
from DAO.Cliente_dao import ClienteDAO
from DAO.Funcionarios_dao import FuncionarioDAO
from DAO.Animal_dao import AnimalDAO
from DAO.Consulta_dao import ConsultaDAO
from DAO.login_dao import LoginDAO
from DAO.criar import criar_banco, criar_tabelas
from DAO.inserir_dados_mestres import inserir_dados_mestre
from DAO.Historico_dao import HistoricoDAO
import re


app = Flask(__name__)
app.secret_key = 'chave-secreta'
status_usuario = False
classificacao = ''


#-----------------------#
#---------LOGIN---------#
#-----------------------#

@app.route('/')
def login_page():
    return render_template('Login.html')

@app.route('/login', methods=['POST'])
def processar_login():
    global classificacao
    global chave_usuario
    global status_usuario

    usuario = request.form.get('usuario_login')
    senha = request.form.get('senha_login')

    teste_login = Login(     
            id_login =None,
            fk_funcionario=usuario,       
            senha=senha,               
            fk_cpf=usuario,                
            fk_cargo=None
    )

    dao = LoginDAO()
    verificacao_login = dao.validar_login(teste_login)

    try:
        if verificacao_login != []:
            status_usuario = True

            if verificacao_login[0][0]:
                classificacao = 'cliente'
                chave_usuario = verificacao_login[0][0]
                return redirect(url_for('menu_cliente_page'))
            else:
                classificacao = 'funcionario'
                chave_usuario = verificacao_login[0][1]
                print(chave_usuario)
                return redirect(url_for('menu_funcionario_page'))
        else:
            return redirect(url_for('login_page'))  # adiciona isto

    except:
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
            id_login =None,
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
        dao.inserir_login(novo_login)

        flash('Cadastro Realizado!', 'sucess')
        return redirect(url_for('login_page'))


    return redirect(url_for('register_page'))

    
#---------------------------------------#
#---------REGISTRAR FUNCIONÁRIO---------#
#---------------------------------------#

@app.route('/registrar_funcionario')
def register_func_page():
   return render_template('Register_funcionario.html')


@app.route('/register_func', methods=['POST']) #cpf removido 
def processar_register_func():
    nome        = request.form.get('nome_register')
    senha       = request.form.get('senha_register')
    data_nasc   = request.form.get('nasc_register')
    cargo       = request.form.get('cargo_register') 

    celular     = request.form.get('celular_register')
    email       = request.form.get('email_register')

    bairro      = request.form.get('bairro_register')or None
    rua         = request.form.get('rua_register')or None
    complemento = request.form.get('complemento_register') or None

    nome_valido = tratar_dados.validar_nome(nome)
    senha_valida = tratar_dados.validar_senha(senha)
    
    celular = re.sub(r"\D", "", celular)

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
    
    bairro_valido = (
    tratar_dados.validar_bairro(bairro)
    if bairro else True
    )

    rua_valida = (
        tratar_dados.validar_rua(rua)
        if rua else True
    )

    complemento_valido = (
        tratar_dados.validar_complemento(complemento)
        if complemento else True
    )

    if nome_valido == False:
        flash("Nome inválido", "error")
    if senha_valida == False:
        flash("Senha inválida, mínimo de 6 digitos e pelo menos 1 caracter especial", "error")
    if celular_valido == False:
        flash("celular inválido", "error")
    if email_valido == False:
        flash("email inválido", "error")
    if bairro_valido == False:
        flash("Bairro inválido", "error")
    if rua_valida == False:
        flash("Rua inválido", "error")
    if cargo_valido == False:
        flash("Selecione um cargo")

    print(nome_valido, nome_valido, data_nasc_valida, cargo_valido, celular_valido, email_valido, bairro_valido,
          rua_valida, complemento_valido)
    
    if (nome_valido and senha_valida and data_nasc_valida and 
        cargo_valido and celular_valido and email_valido and 
        bairro_valido and rua_valida and complemento_valido):

        cargo = int(cargo)

        novo_funcionario = funcionario(
            id_funcionario = None,
            fk_id_cargo = cargo,
            nome_funcionario = nome,
            num_celular = celular,
            email = email_limpo,
            bairro = bairro,
            rua = rua,
            complemento = complemento,
            dt_nascimento = data_nasc_valida
        )
        
        dao = FuncionarioDAO()
        id_func = dao.inserir_funcionario(novo_funcionario)
    
        novo_login = Login(     
            id_login = None,
            fk_funcionario=id_func,       
            senha=senha,               
            fk_cpf=None,                
            fk_cargo=cargo
        )
        
        dao.inserir_login(novo_login)

        return redirect(url_for('login_page'))
    else:
        print('puta que pariu quero dormi duas da manhã vai se fuder')
        return redirect(url_for('register_func_page'))
#------------------------------#
#---------MENU CLIENTE---------#
#------------------------------#

@app.route('/menu_cliente')
def menu_cliente_page():
    if status_usuario == True:
        return render_template('Menu_cliente.html')
    else:
        print('oi')
        return redirect(url_for('login_page'))
    

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
    global status_usuario
    status_usuario = False

    return redirect(url_for('login_page'))

#----------------------------------#
#---------MENU FUNCIONÁRIO---------#
#----------------------------------#

@app.route('/menu_funcionario')
def menu_funcionario_page():
    if status_usuario == True:
        return render_template('Menu_funcionario.html')
    
    else:
        return redirect(url_for('login_page'))

@app.route('/menu_fucionario_gerenciar_consulta', methods=['GET'])
def processar_menu_funcionario_gerenciar_consulta():
    return redirect(url_for('gerenciar_consulta_page'))

#-------------------------------------#
#---------GERENCIAR CONSULTAS---------#
#-------------------------------------#

@app.route('/Gerenciar_consulta')
def gerenciar_consulta_page():
    if status_usuario == True:
        dao = ConsultaDAO()
        lista_tabela = dao.buscar_consultas_gerenciar()
        lista_dashboard = dao.buscar_totais_dashboard()

        return render_template('Gerenciar_consulta.html', lista_tabela=lista_tabela, lista_dashboard=lista_dashboard)
    
    else:
        return redirect(url_for('login_page'))

@app.route('/concluir_consulta', methods=['POST'])
def processar_concluir_consulta():
    id_consulta_html = request.form.get('id_consulta')
    
    dao = ConsultaDAO()
    dao.concluir_consulta(id_consulta_html)

    return redirect(url_for('gerenciar_consulta_page'))

@app.route('/deletar_consulta', methods=['POST'])
def processar_deletar_consulta():
    id_consulta_html = request.form.get('id_consulta')
   
    dao = ConsultaDAO()
    dao.deletar_consulta(id_consulta_html)

    return redirect(url_for('gerenciar_consulta_page'))

#---------------------------------#
#---------MARCAR CONSULTA---------#
#---------------------------------#

@app.route('/marcar_consulta')
def marcar_consulta_page():
    if status_usuario == True:
        return render_template('Marcar_consulta.html')
    
    else:
        return redirect(url_for('login_page'))
    
@app.route('/Voltar', methods=['GET'])
def processar_voltar_menu_cliente():
    if classificacao == 'cliente':
        return redirect(url_for('menu_cliente_page'))
    elif classificacao == 'funcionario':
        return redirect(url_for('menu_funcionario_page'))

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
    nome_valido = tratar_dados.validar_nome(nome_animal)
    data_valida = tratar_dados.validar_data_consulta(data_consulta)
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
            
    if (tipo_valido and especie_valida and nome_valido and data_valida):
        if classificacao == 'cliente':
            cpf = chave_usuario
        elif classificacao == 'funcionario':
            cpf = None

        print(cpf)

        novo_animal = Animal(
                    id_animal   = None,
                    fk_cpf      = cpf,
                    nome_animal = nome_animal,
                    raca        = None,          
                    especie     = especie_final,
                    genero      = "N",            
                    peso        = 0.0             
        )

        dao = AnimalDAO()
        id_pet = dao.inserir_animal(novo_animal)
    
        nova_consulta = Consulta(
            id_consulta         = None,
            fk_animal           = id_pet,  
            fk_cpf              = cpf,
            fk_funcionario      = None,
            fk_tipo_consulta    = int(tipo_consulta),
            dt_consulta         = data_valida,
            hr_consulta         = hora_valida
        )
 
        dao = ConsultaDAO()
        dao.inserir_consulta(nova_consulta)
        
        flash('Consulta marcarda!', 'sucess')
        if classificacao == 'cliente':
            return redirect(url_for('menu_cliente_page'))
        elif classificacao == 'funcionario':
            return redirect(url_for('menu_funcionario_page'))
    
    if tipo_valido == False:
        flash('Tipo da consulta inválido', 'error')

    if nome_valido == False:
        flash('Nome inválido', 'error')

    if data_valida == False:
        flash('Data inválido', 'error')

    if hora_valida == False:
        flash('Hora inválido', 'error')

    if especie_valida == False:
        flash('Espécie inválido', 'error')


    return redirect(url_for('marcar_consulta_page'))

#-------------------------------------#
#---------ACOMPANHAR CONSULTA---------#
#-------------------------------------#

@app.route('/acompanhar_consulta')
def acompanhar_consulta_page():
    if status_usuario == True:
        dao = ConsultaDAO()

        if classificacao == 'cliente':
            lista_acompanhar_consulta = dao.acompanhar_consulta(chave_usuario)

        elif classificacao == 'funcionario':
            lista_acompanhar_consulta = dao.acompanhar_funcionario(chave_usuario)
        
        return render_template('Acompanhar_consulta.html', lista_acompanhar_consulta=lista_acompanhar_consulta)
    
    else:
        return redirect(url_for('login_page'))
    
#-------------------------------------#
#---------Verificar Histórico---------#
#-------------------------------------#

@app.route('/historico_consulta')
def historico_page():
    if status_usuario == True:
        dao = HistoricoDAO()

        if classificacao == 'cliente':
            lista_historico = dao.mostrar_historico_cliente(chave_usuario)

        elif classificacao == 'funcionario':
            lista_historico = dao.mostrar_historico_funcionario()

        return render_template('historico.html', lista_historico=lista_historico)
    
    else:
        return redirect(url_for('login_page'))
    

@app.route('/filtro', methods=['POST'])
def processar_filtro():
    filtro = request.form.get('txt_filtro')

    return redirect(url_for('historico_page'))

#---------------------#
#---------APP---------#
#---------------------#

if __name__ == '__main__':
    criar_banco()
    criar_tabelas()
    inserir_dados_mestre()
    app.run(debug=True)