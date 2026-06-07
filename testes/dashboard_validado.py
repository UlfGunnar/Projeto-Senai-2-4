import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DAO.Dashboard_dao import Tipos_de_consulta

dao = Tipos_de_consulta()

somar = dao.listar_consultas()

for c in somar:
    print(c)
