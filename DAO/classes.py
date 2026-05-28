class Cliente():
    def __init__(self, cpf: str,nome_cliente: str, email: str, numero: int, bairro: str, rua: str, celular: str, complemento: str ):
        self.nome_cliente = nome_cliente
        self.cpf = cpf
        self.celular = celular
        self.email = email
        self.bairro = bairro
        self.rua = rua
        self.complemento = complemento
        self.numero = numero

class Animal():
    def __init__(self, id_animal: int, fk_cpf: str, nome_animal: str, raca: str, especie: str, genero: str, peso: float):
        self.id_animal = id_animal
        self.fk_cpf = fk_cpf
        self.nome_animal = nome_animal
        self.raca = raca
        self.especie = especie
        self.genero = genero
        self.peso = peso
        
class Medico():
    #data_nasc = Date
    def __init__(self, matricula_medico: int, nome_medico: str, num_celular: str, rua: str, complemento: str, dt_nascimento: str, email: str, bairro: str):
        self.matricula_medico = matricula_medico
        self.nome_medico = nome_medico
        self.dt_nascimento = dt_nascimento
        self.num_celular = num_celular
        self.email = email
        self.bairro = bairro
        self.rua = rua
        self.complemento = complemento

class Secretaria():
    def __init__(self, matricula_secretaria: int, nome_secretaria: str, dt_nascimento: str, email: str, rua: str, num_celular: str, complemento: str, bairro: str):
        self.matricula_medico = matricula_secretaria
        self.nome_medico = nome_secretaria
        self.dt_nascimento = dt_nascimento
        self.num_celular = num_celular
        self.email = email
        self.bairro = bairro
        self.rua = rua
        self.complemento = complemento
class Consulta():
    #data = date
    #hora = date
    def __init__(self, id_consulta: int, fk_matricula_medico: int, fk_animal: int, fk_cpf: str, fk_tipo_consulta: int, dt_consulta, hr_consulta):
        self.id_consulta = id_consulta
        self.fk_animal = fk_animal
        self.fk_cpf = fk_cpf
        self.fk_matricula_medico = fk_matricula_medico
        self.fk_tipo_consulta = fk_tipo_consulta
        self.dt_consulta = dt_consulta
        self.hr_consulta = hr_consulta

class Tipo_de_consulta():
    def __init__(self, id_tipo: int, id_consulta: int, finalidade: str, valor: float):
        self.id_tipo = id_tipo
        self.id_consulta = id_consulta
        self.finalidade = finalidade
        self.valor = valor

class Login():
    def __init__(self, id_conta: int, fk_cpf: str, fk_matricula_secretaria: int, fk_matricula_medico: int, usuario: str, senha: str):
        self.id_conta = id_conta
        self.fk_cpf = fk_cpf
        self.fk_matricula_secretaria = fk_matricula_secretaria
        self.fk_matricula_medico = fk_matricula_medico
        self.usuario = usuario
        self.senha = senha

class Historico():
    #data_consulta = date
    #hora_consulta = date
    def __init__(self, id_historico: int, fk_animal: int, fk_tipo: int, fk_cpf: str, fk_consulta: int, remedio: str, diagnostico: str, data, hora):
        self.id_historico = id_historico
        self.fk_animal = fk_animal
        self.fk_cpf = fk_cpf
        self.fk_tipo = fk_tipo
        self.fk_consulta = fk_consulta
        self.diagnostico = diagnostico
        self.remedio = remedio
        self.data = data
        self.hora = hora

