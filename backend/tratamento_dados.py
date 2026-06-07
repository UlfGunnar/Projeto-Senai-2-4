from flask import flash
import re 
from email_validator import validate_email, EmailNotValidError
from datetime import datetime

#------------------------------------
#VALIDAÇÃO DA TELA DE REGISTROS
#------------------------------------

"""""
6 caracteres minimos
1 caracter especial
"""""
def validar_senha(senha): #Testado
    senha = senha
    senha_sem_espaço = senha.replace(" ", "")
    senha_especial = any(not c.isalnum() for c in senha_sem_espaço)
    if senha_especial and len(senha_sem_espaço) >= 6:
        return True
    else:
        return False
    
    #validado, vai devolver o nome sem espaços (corretamente) "igor flores" 
def validar_nome(nome):
        nome = nome.strip()
        if nome.replace(" ", "").isalpha():
            return True
        else:
            return False
    
def validar_celular(celular): #tá dale
    numero_tratado = celular.strip()
    try:
        numero_tratado = re.sub(r"\D", "", celular) #remove tudo que não é número pra ficar certinho pro banco de dados
    except (NameError, TypeError): #garante que tudo existe e o texto é válido (pouco importante né)
        return False
    if len(numero_tratado) == 11: #claramente limita a 11 dígitos
        return True
    else:
        return False

def validar_email(email): #tá funfando
    try:
        email_info = validate_email(email) #verifica se o email é real e se está escrito correto (só tem um @ e tals)

        email_limpo = email_info.normalized #remove espaços e deixa em letras mínusculas pra ficar menos bagunçado
        return True, email_limpo
        
    except EmailNotValidError:
        return False #não deixa o troço explodir
    
def validar_bairro(bairro): #tá correto
    bairro = bairro.strip()
    bairro_padrao = r"^[A-Za-zÀ-ÿ0-9\-.'ºª]+( [A-Za-zÀ-ÿ0-9\-.'ºª]+)*$"
    verificando = re.fullmatch(bairro_padrao, bairro)
    if verificando:
        return True
    else:
        return False

def validar_numero(numero_casa): #tá rolando
    #maior número pode ter 5 dígitos
    #só pode número
    numero_casa = numero_casa or ""

    if not numero_casa:
        return True

    if not numero_casa.isdecimal():
        return False

    if len(numero_casa) > 5:
        return False

    return True
    
def validar_rua(rua): #tá funcionando
    #não tem muito o que validar, tem rua com caracter especial e coisa do tipo então meh
    rua = rua.strip()
    rua_padrao = r"^[A-Za-zÀ-ÿ0-9\-.'ºª]+( [A-Za-zÀ-ÿ0-9\-.'ºª]+)*$" #indica o que é aceito na string
    verificando = re.fullmatch(rua_padrao, rua) #re.match tá vendo se tá batendo com o que é aceito na string
    if verificando:
        return True
    else:
        return False
    
def validar_complemento(complemento): #tá dale (2)
    #sem caractere especial 
    #sem espaço no começo e no fim
    complemento = complemento.strip()
    valor_regular = r"[A-Za-zÀ-ÿ0-9,.\-/]+(\s[A-Za-zÀ-ÿ0-9,.\-/]+)*" #é um padrão indicando o que é aceito
    return bool(re.fullmatch(valor_regular, complemento)) #verifica se tá compatível com o que é aceito

def validar_cpf(cpf): #tá indo
    #11 dígitos
    #só número
    cpf = cpf.strip()# tira espaço do lado
    cpf = cpf.replace(".", "").replace("-", "")
    if cpf.isdecimal() and len(cpf) == 11: #só garante que vai seguir o padrão que a gente quer
        return True
    else:
        return False

#------------------------------------
#VALIDAÇÃO DA TELA DE MARCAR CONSULTA
#------------------------------------

def validar_outra_especie_animal(outra_especie_animal): #está funfando
    outra_especie_animal = outra_especie_animal.strip()
    outra_especie_animal_padrao = outra_especie_animal_padrao = r"^[A-Za-zÀ-ÿ]+(\s[A-Za-zÀ-ÿ]+)?$"
    verificando = re.fullmatch(outra_especie_animal_padrao, outra_especie_animal)
    if verificando:
        return True
    else:
        return False

#data e hora (usar datetime provavelmente)
    
def validar_data(data_consulta):
    try:
        # Mudamos de %m/%d para %d/%m
        data = datetime.strptime(data_consulta, "%d/%m/%Y")
        return data.strftime("%Y-%m-%d")
    except ValueError:
        return False

def validar_horario(horario): #tá funfando
    try: 
        hora = datetime.strptime(horario, "%H:%M")
        return hora.strftime("%H:%M:%S")
    except ValueError:
        return False

def complemento_consulta(complemento): #funcionando
    complemento = complemento.strip()
    padrao_complemento = r"[A-Za-zÀ-ÿ0-9,.\-/]+(\s[A-Za-zÀ-ÿ0-9,.\-/]+)*"
    return bool(re.fullmatch(padrao_complemento, complemento))
 
def validar_bairro(bairro): #tá bom
    bairro = bairro.strip() if bairro else ""
    # Aceita letras (com acento), números e espaços entre as palavras
    padrao = r"[A-Za-zÀ-ÿ0-9]+(\s[A-Za-zÀ-ÿ0-9]+)*"
    return bool(re.fullmatch(padrao, bairro))

def validar_rua(rua): #tá funfando
    rua = rua.strip() if rua else ""
    # Aceita letras, números, pontos (ex: R.) e hífens
    padrao = r"[A-Za-zÀ-ÿ0-9.,\-]+(\s[A-Za-zÀ-ÿ0-9.,\-]+)*"
    return bool(re.fullmatch(padrao, rua))

def validar_numero(numero_casa):
    if not numero_casa:
        return True

    if not numero_casa.isdecimal():
        return False

    if len(numero_casa) > 5:
        return False

    return True

def validar_proprio_endereco(endereco): #correto
    # Geralmente é um booleano do checkbox (True/False ou "on"/None)
    # Se vier como string do form, garante que não tá vazio
    if endereco:
        return True
    return False 

#------------------------------------------------------------
#FLASH (mensagem de erro)
#------------------------------------------------------------