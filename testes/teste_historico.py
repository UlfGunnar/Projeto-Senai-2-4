import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connection.connection import get_connection
from DAO.Historico_dao import HistoricoDAO
from DAO.classes import Historico

dao = HistoricoDAO()

historico = Historico(
    1,
    1,
    "12345678901",
    1,
    "Remédio X",
    "Diagnóstico Y",
    "2026-05-15",
    "09:00:00"
)

dao.inserir_historico(historico)
print("Histórico inserido com sucesso!")