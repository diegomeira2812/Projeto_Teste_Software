import sqlite3
from utils.config_loader import carregar_config

def get_connection():
# retorna uma conexão SQLite conforme o arquivo de configuração
    config = carregar_config()
    db_path = config.get("db_path", "stockmaster.db")
    return sqlite3.connect(db_path)
