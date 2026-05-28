import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connection.connection import get_connection
from DAO.Tipos_de_consulta_dao import TiposDeConsultaDAO    
from DAO.classes import Tipo_de_consulta

dao = TiposDeConsultaDAO()

tipo_consulta = Tipo_de_consulta(
    1,
    "Consulta de rotina",
    150.00
)

dao.inserir_tipo_consulta(tipo_consulta)
print("Tipo de consulta inserido com sucesso!")