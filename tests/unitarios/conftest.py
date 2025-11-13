# tests/conftest.py
import os
import pytest
from utils.db_connection import DB_PATH

@pytest.fixture(autouse=True)
def limpar_banco():
    """
    Limpa o banco de dados antes e depois de cada teste.
    Garante que cada teste tenha um ambiente isolado e independente.
    """
    # Antes do teste — remove o banco se já existir
    if os.path.exists(DB_PATH):
        try:
            os.remove(DB_PATH)
        except PermissionError:
            pass  # Ignora se o arquivo estiver em uso momentaneamente

    yield  # Aqui os testes são executados

    # Depois do teste — remove novamente
    if os.path.exists(DB_PATH):
        try:
            os.remove(DB_PATH)
        except PermissionError:
            pass
