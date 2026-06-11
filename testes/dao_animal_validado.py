import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connection.connection import get_connection
from DAO.Animal_dao import AnimalDAO
from backend.classes import Animal

dao = AnimalDAO()

animal = Animal(
    None,
    "12345678901",
    "rex",
    "Pitbull",
    "Cachorro",
    "M",
    15.5
)

dao.inserir_animal(animal)

print("Animal inserido com sucesso!")