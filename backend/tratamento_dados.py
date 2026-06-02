from flask import flash
import re 
from email_validator import validate_email, EmailNotValidError

#------------------------------------
#VALIDAÇÃO DA TELA DE REGISTROS
#------------------------------------

"""""
6 caracteres minimos
1 caracter especial
"""""
def validar_senha(self, senha): #Testado
    self.senha = senha
    senha_sem_espaço = senha.replace(" ", "")
    senha_especial = any(not c.isalnum() for c in senha_sem_espaço)
    if senha_especial and len(senha_sem_espaço) >= 6:
        return True
    else:
        return False
    
class validar_nome: #validado, vai devolver o nome sem espaços (corretamente) "igor flores" 
    def validar_nome(self, nome):
        self.nome = nome.strip()
        if self.nome.replace(" ", "").isalpha():
            return True
        else:
            return False
    
def validar_celular(self, numero, numero_tratado): #tá dale
    self.numero = numero
    self.numero_tratado = numero_tratado
    try:
        numero_tratado = re.sub(r"\D", "", numero) #remove tudo que não é número pra ficar certinho pro banco de dados
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
    if not numero_casa.isdecimal():
        return False
    if len(numero_casa) > 5:
        return False
    else:
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
    
def complemento(complemento): #tá dale (2)
    #sem caractere especial 
    #sem espaço no começo e no fim
    complemento = complemento.strip()
    valor_regular = r"[A-Za-zÀ-ÿ0-9,.\-/]+(\s[A-Za-zÀ-ÿ0-9,.\-/]+)*" #é um padrão indicando o que é aceito
    return bool(re.fullmatch(valor_regular, complemento)) #verifica se tá compatível com o que é aceito

def validar_cpf(cpf):
    #11 dígitos
    #só número
    cpf = cpf.strip()
    if cpf.isdecimal() and len(cpf) == 11:
        return True
    else:
        return False

