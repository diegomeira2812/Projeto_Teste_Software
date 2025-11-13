from contextlib import contextmanager
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "teste.db")

@contextmanager
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    init_db(conn)
    try:
        yield conn
    finally:
        conn.close()

def init_db(conn):
    cursor = conn.cursor()
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS fornecedores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            contato TEXT NOT NULL,
            cnpj TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL,
            fornecedor_id INTEGER
        );
    """)
    conn.commit()
