from flask import flash
import re
# Registro
"""""
6 caracteres minimos
1 caracter especial
"""""
def validar_senha(self, senha):
    self.senha = senha
    senha_especial = any(not c.isalnum() for c in senha)
    if senha_especial and len(senha) >= 6:
        return True
    else:
        return False
    
def validar_nome(self, nome):
    self.nome = nome
    if nome.replace(" ", "").isalpha():
        return True
    else:
        return False
    
def validar_celular(self,numero, numero_tratado):
    self.numero = numero
    self.numero_tratado = numero_tratado
    try:
        numero_tratado = re.sub(r"\D", "", numero)
    except:
        #inserir aqui alguma coisa
    if len(numero_tratado) == 11:
        return False
    else:
        return True
