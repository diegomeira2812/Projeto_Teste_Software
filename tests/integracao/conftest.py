# tests/conftest.py
import pytest
import os
import sqlite3
from utils.db_connection import get_connection

@pytest.fixture(autouse=True)
def limpar_banco():
    """Recria o banco antes de cada teste sem forçar remoção enquanto está aberto."""
    db_path = "stockmaster.db"

    # Fecha conexões antes de apagar
    try:
        conn = sqlite3.connect(db_path)
        conn.close()
    except Exception:
        pass

    # Remove o arquivo se possível
    if os.path.exists(db_path):
        try:
            os.remove(db_path)
        except PermissionError:
            pass  # Em último caso, deixa o arquivo; as tabelas serão recriadas

    # Garante que o banco seja limpo
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS produtos")
        cursor.execute("DROP TABLE IF EXISTS fornecedores")
        conn.commit()

    yield

    # Após o teste, tenta apagar novamente
    try:
        if os.path.exists(db_path):
            os.remove(db_path)
    except PermissionError:
        pass
