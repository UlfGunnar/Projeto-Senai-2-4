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
        
class funcionario():
    #data_nasc = date
    def __init__(self, id_funcionario: int, fk_id_cargo: int, nome_funcionario: str, num_celular: str, email: str, bairro: str, rua: str, complemento: str, dt_nascimento):
        self.id_funcionario = id_funcionario
        self.fk_id_cargo = fk_id_cargo
        self.nome_funcionario = nome_funcionario
        self.num_celular = num_celular
        self.email = email
        self.bairro = bairro
        self.rua = rua
        self.complemento = complemento
        self.dt_nascimento = dt_nascimento

class cargo():
    def __init__(self, id_cargo: int, nome_cargo: str):
        self.id_cargo = id_cargo
        self.nome_cargo = nome_cargo
        
class Consulta():
    #data = date
    #hora = date
    def __init__(self, id_consulta: int, fk_animal: int,  fk_cpf: str, fk_funcionario: int, fk_tipo_consulta: int, dt_consulta, hr_consulta):
        self.id_consulta = id_consulta
        self.fk_animal = fk_animal
        self.fk_cpf = fk_cpf
        self.fk_funcionario = fk_funcionario
        self.fk_tipo_consulta = fk_tipo_consulta
        self.dt_consulta = dt_consulta
        self.hr_consulta = hr_consulta

class Tipo_de_consulta():
    def __init__(self, id_consulta: int, finalidade: str, valor: float):
        self.id_consulta = id_consulta
        self.finalidade = finalidade
        self.valor = valor

class Login():
    def __init__(self, id_login: int, fk_funcionario: int, fk_cpf: str, fk_cargo: int, senha: str):
        self.id_login = id_login
        self.fk_funcionario = fk_funcionario
        self.fk_cpf = fk_cpf
        self.fk_cargo = fk_cargo
        self.senha = senha
        

class Historico():
    #data_consulta = date
    #hora_consulta = date
    def __init__(self, id_historico: int, fk_animal: int, fk_cpf: str, fk_tipo: int, fk_consulta: int, diagnostico: str, remedio: str, data, hora):
        self.id_historico = id_historico
        self.fk_animal = fk_animal
        self.fk_cpf = fk_cpf
        self.fk_tipo = fk_tipo
        self.fk_consulta = fk_consulta
        self.diagnostico = diagnostico
        self.remedio = remedio
        self.data = data
        self.hora = hora

