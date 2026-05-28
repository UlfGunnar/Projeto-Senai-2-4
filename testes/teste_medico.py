import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connection.connection import get_connection
from DAO.Medico_dao import MedicoDAO
from DAO.classes import Medico

dao = MedicoDAO()

medico = Medico(
    1,
    "Dr. João Silva",
    "47999999999",
    "joao.silva_dogtor@gmail.com",
    "Imuit",
    "XV de Piracicaba",
    "1998-05-15",
)

dao.inserir_medico(medico)

print("Médico inserido com sucesso!")