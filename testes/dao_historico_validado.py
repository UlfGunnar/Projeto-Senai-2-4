import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connection.connection import get_connection
from DAO.Historico_dao import HistoricoDAO
from backend.classes import Historico

dao = HistoricoDAO()

historico = Historico(
    None,
    4,
    "12345678901",
    1,
    34,
    "Remédio X",
    "Diagnóstico Y",
    "2026-06-19",
    "08:30:00"
)

dao.inserir_historico(historico)
print("Histórico inserido com sucesso!")