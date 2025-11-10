
import sqlite3
from models.fornecedor import Fornecedor
from utils.db_connection import get_connection

class FornecedorRepository:
# camada de acesso a dados para fornecedores

    def __init__(self):
        self._criar_tabela()

    def _criar_tabela(self):
        with get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS fornecedores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    contato TEXT,
                    cnpj TEXT NOT NULL
                );
            """)

    def listar_todos(self):
        with get_connection() as conn:
            rows = conn.execute("SELECT * FROM fornecedores").fetchall()
            return [Fornecedor(*row) for row in rows]

    def inserir(self, nome: str, contato: str, cnpj: str):
        with get_connection() as conn:
            conn.execute("""
                INSERT INTO fornecedores (nome, contato, cnpj)
                VALUES (?, ?, ?)
            """, (nome, contato, cnpj))
            conn.commit()
