import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connection.connection import get_connection
from DAO.Cliente_dao import ClienteDAO
from DAO.classes import Paciente

dao = ClienteDAO()

cliente = Paciente(
    "12345678901",
    "Pedrão Luxeba",
    "pedrolr2060@gmail.com",
    "Itmiu",
    "Rua 13 de China",
    "123",
    "Ap 102",
    "47999999999"
)

dao.inserir_cliente(cliente)

print("Cliente inserido com sucesso!")