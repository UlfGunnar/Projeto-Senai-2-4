import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connection.connection import get_connection
from DAO.Funcionarios_dao import FuncionarioDAO
from backend.classes import funcionario

dao = FuncionarioDAO()

funcionario = funcionario(
    None,
    1,
    "João Silva",
    "4799999999",
    "joao.silva@email.com",
    "Centro",
    "Rua Exemplo",
    "Apartamento 101",
    "1990-01-01"
)

dao.inserir_funcionario(funcionario)
print("Funcionário inserido com sucesso!")