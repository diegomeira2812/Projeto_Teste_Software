import json
import os

def carregar_config() -> dict:
# carrega o arquivo de configuração JSON
    caminho = "config.json"
    if not os.path.exists(caminho):
        return {"db_path": "stockmaster.db", "log_file": "stockmaster.log"}
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)
