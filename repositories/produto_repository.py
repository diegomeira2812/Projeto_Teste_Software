import sqlite3
from models.produto import Produto
from utils.db_connection import get_connection

class ProdutoRepository:
# camada de acesso a dados para produtos

    def __init__(self):
        self._criar_tabela()

    def _criar_tabela(self):
        with get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    preco REAL NOT NULL,
                    quantidade INTEGER NOT NULL,
                    fornecedor_id INTEGER
                );
            """)

    def listar_todos(self):
        with get_connection() as conn:
            rows = conn.execute("SELECT * FROM produtos").fetchall()
            return [Produto(*row) for row in rows]

    def inserir(self, nome: str, categoria: str, preco: float, quantidade: int, fornecedor_id: int):
        with get_connection() as conn:
            conn.execute("""
                INSERT INTO produtos (nome, categoria, preco, quantidade, fornecedor_id)
                VALUES (?, ?, ?, ?, ?)
            """, (nome, categoria, preco, quantidade, fornecedor_id))
            conn.commit()

    def atualizar_quantidade(self, produto_id: int, nova_qtd: int):
        with get_connection() as conn:
            conn.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_qtd, produto_id))
            conn.commit()

    def remover(self, produto_id: int):
        with get_connection() as conn:
            conn.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
            conn.commit()

    def buscar_por_categoria(self, categoria: str):
        with get_connection() as conn:
            rows = conn.execute("SELECT * FROM produtos WHERE categoria = ?", (categoria,)).fetchall()
            return [Produto(*row) for row in rows]
