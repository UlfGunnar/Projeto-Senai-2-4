class Cliente():
    def __init__(self, cpf: str, nome: str, email: str, numero: int, bairro: str, rua: str, celular: str, complemento: str):
        self.cpf = cpf = cpf
        self.nome = nome
        self.email = email
        self.numero = numero
        self.bairro = bairro
        self.rua = rua
        self.celular = celular
        self.complemento = complemento

class Animal():
    def __init__(self, id_animal, cpf: str, nome: str, raca: str, especie: str, genero: str, peso: float):
        self.id_animal = id_animal
        self.cpf = cpf
        self.nome = nome
        self.raca = raca
        self.especie = especie
        self.genero = genero 
        self.peso = peso

class Medico():
    #data_nasc = date
    def __init__(self, matricula_medico, nome: str, numero: str, rua: str, complemento: str, data_nasc, email: str, celular: str):
        self.matricula_medico = matricula_medico
        self.nome = nome
        self.numero = numero
        self.rua = rua
        self.complemento = complemento
        self.data_nasc = data_nasc
        self.email = email
        self.celular = celular

class Secretaria():
    #data_nasc = date
    def __init__(self, matricula_secretaria, nome: str, data_nasc, email: str, rua: str, celular: str, complemento: str, numero: str):
        self.matricula_secretaria = matricula_secretaria
        self.nome = nome
        self.data_nasc = data_nasc
        self.email = email
        self.rua = rua
        self.celular = celular
        self.complemento = complemento
        self.numero = numero

class Consulta():
    #"data" e "hora" utilizarão date
    def __init__(self, id_consulta, matricula_medico: int, id_animal: int, cpf: str, tipo_consulta: str, data, hora, residencial: bool):
        self.id_consulta = id_consulta
        self.matricula_medico = matricula_medico
        self.id_animal = id_animal 
        self.cpf = cpf
        self.tipo_consulta = tipo_consulta
        self.data = data
        self.hora = hora
        self.residencial = residencial

class Tipo_consultas():
    def __init__(self, id_tipo, id_consulta: int, tipo: str, valor: float):
        self.id_tipo = id_tipo
        self.id_consulta = id_consulta
        self.tipo = tipo
        self.valor = valor

class Login():
    def __init__(self, id_conta, cpf: str, matricula_secretaria: int, matricula_medico: int, usuario: str, senha: str):
        self.id_conta = id_conta
        self.cpf = cpf
        self.matricula_secretaria = matricula_secretaria
        self.matricula_medico = matricula_medico
        self.usuario = usuario
        self.senha = senha

class Historico():
    #data_consulta = date
    #hora_consulta = date
    def __init__(self, id_historico, id_animal: int, id_tipo: int, cpf: str, id_consulta: int, remedio: str, diagnostico: str, data_consulta, hora_consulta):
        self.id_historico = id_historico
        self.id_animal = id_animal
        self.id_tipo = id_tipo
        self.cpf = cpf
        self.id_consulta = id_consulta
        self.remedio = remedio
        self.diagnostico = diagnostico
        self.data_consulta = data_consulta
        self.hora_consulta = hora_consulta

