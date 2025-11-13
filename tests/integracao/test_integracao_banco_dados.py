# tests/test_integracao_banco_dados.py
from repositories.produto_repository import ProdutoRepository
from utils.db_connection import get_connection
import pytest

pytestmark = pytest.mark.integration

def test_conexao_e_persistencia():
    repo = ProdutoRepository()
    repo.inserir("Pendrive", "Informática", 50.0, 100, 1)

    # Conectar diretamente e verificar persistência real
    with get_connection() as conn:
        cursor = conn.execute("SELECT COUNT(*) FROM produtos")
        count = cursor.fetchone()[0]
        assert count == 1
