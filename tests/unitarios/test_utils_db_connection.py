from utils.db_connection import get_connection
from unittest.mock import patch
import sqlite3
import pytest

def test_conexao_banco_valida():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        assert cursor.fetchone()[0] == 1

def test_erro_conexao_simulado():
    with patch("sqlite3.connect", side_effect=sqlite3.OperationalError):
        with pytest.raises(sqlite3.OperationalError):
            with get_connection():
                pass
