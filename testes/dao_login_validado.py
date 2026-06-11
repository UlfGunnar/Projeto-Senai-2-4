import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connection.connection import get_connection
from DAO.login_dao import LoginDAO
from backend.classes import Login

dao = LoginDAO()

login = Login(
    None,
    2,
    "12625627891",
    1,
    "joao@"
)

dao.inserir_login(login)
print("Login inserido com sucesso!")