from flask import flash
import re
# Registro
"""""
6 caracteres minimos
1 caracter especial
"""""
def validar_senha(self, senha): #
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
    
def validar_celular(self, numero, numero_tratado):
    self.numero = numero
    self.numero_tratado
    try:
        numero_tratado = re.sub(r"\D", "", numero)
    except (NameError, TypeError):
        return False
    if len(numero_tratado) == 11:
        return True
    else:
        return False

def validar_email(self, email):
    self.email = email
