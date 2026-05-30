import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connection.connection import get_connection
from DAO.Consulta_dao import ConsultaDAO
from DAO.classes import Consulta

dao = ConsultaDAO()

consulta = Consulta(
    None,
    2,
    4,
    "12345678901",
    1,
    "2026-06-19",
    "08:30:00"
)

dao.inserir_consulta(consulta)

print("Consulta inserida com sucesso!")