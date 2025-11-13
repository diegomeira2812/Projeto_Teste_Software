import io
from unittest.mock import patch
import main

def test_menu_opcoes_exibe_corretamente():
    saida = io.StringIO()
    with patch("sys.stdout", new=saida):
        with patch("builtins.input", side_effect=["0"]):
            try:
                main.main()
            except SystemExit:
                pass
    texto = saida.getvalue()
    assert "--- StockMaster ---" in texto
    assert "Gerenciar Produtos" in texto

def test_menu_sair_funciona():
    saida = io.StringIO()
    with patch("sys.stdout", new=saida):
        with patch("builtins.input", side_effect=["0"]):
            try:
                main.main()
            except SystemExit:
                pass
    assert "Saindo do sistema" in saida.getvalue()

def test_navegacao_submenu():
    saida = io.StringIO()
    with patch("sys.stdout", new=saida):
        with patch("builtins.input", side_effect=["1", "0", "0"]):
            try:
                main.main()
            except SystemExit:
                pass
    texto = saida.getvalue()
    assert "--- PRODUTOS ---" in texto
