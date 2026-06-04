import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DAO.Gerir_cons_Func_dao import ConsultaDAO  

dao = ConsultaDAO()

consultas = dao.listar_consultas()

for c in consultas:
    print(c)
