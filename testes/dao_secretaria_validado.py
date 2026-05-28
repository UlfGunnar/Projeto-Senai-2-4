import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connection.connection import get_connection
from DAO.Secretaria_dao import SecretariaDAO
from DAO.classes import Secretaria

dao = SecretariaDAO()

secretaria = Secretaria(
    1,
    "Maria Oliveira",
    "2002-05-15",
    "47999999999",
    "maria.oliveira_dogtor@gmail.com",
    "Anitapolis",
    "Rua das Flores",
    None
)

dao.inserir_secretaria(secretaria)

print("Secretária inserida com sucesso!")