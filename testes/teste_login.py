import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connection.connection import get_connection
from DAO.login_dao import LoginDAO
from DAO.classes import Login

dao = LoginDAO()

login = Login(
    "12345678901",
    1,
    1,
    1,
    "usuario_teste",
    "senha_teste"
)

dao.inserir_login(login)

print("Login inserido com sucesso!")