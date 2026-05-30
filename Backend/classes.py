class paciente():
    def __init__(self, cpf: str,nome: str, email: str, num_casa: int, bairro: str, rua: str, num_tele: str, complemento: str ):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.num_casa = num_casa
        self.bairro = bairro
        self.rua = rua
        self.num_tele = num_tele
        self.complemento = complemento

class animal():
    def __init__(self, id_animal: int, cpf: str, nome: str, raca: str, especie: str, genero: str, peso: float):
        self.id_animal = id_animal
        self.cpf = cpf
        self. nome = nome
        self.raca = raca
        self.especie = especie
        self.genero = genero
        self.peso = peso
        
class consulta():
    def __init__(self, id_consulta: int, matricula_medico: int):


        
