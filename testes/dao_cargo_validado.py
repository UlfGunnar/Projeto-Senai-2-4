import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connection.connection import get_connection
from DAO.Cargo_dao import CargoDAO
from DAO.classes import cargo

dao = CargoDAO()

cargo = cargo(
    None,
    "Veterinário"
)

dao.inserir_cargo(cargo)
print("Cargo inserido com sucesso!")