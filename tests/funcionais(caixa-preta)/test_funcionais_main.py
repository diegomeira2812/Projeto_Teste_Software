# tests/test_funcionais_main.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from services.produto_service import ProdutoService

import io
from unittest.mock import patch
import main


def test_listar_produtos_vazio():
    saida = io.StringIO()
    with patch("sys.stdout", new=saida):
        with patch("builtins.input", side_effect=["1", "1", "0", "0"]):
            try:
                main.main()
            except SystemExit:
                pass
    assert "--- StockMaster ---" in saida.getvalue()


def test_adicionar_e_listar_produto():
    service = ProdutoService()
    # Simula o fluxo: abrir menu → entrar em produtos → adicionar → listar → sair
    entradas = [
        "1",  # menu principal -> produtos
        "2",  # adicionar produto
        "Caneta", "Papelaria", "1.5", "50", "1",
        "1",  # listar
        "0",  # voltar
        "0"   # sair
    ]
    saida = io.StringIO()
    with patch("sys.stdout", new=saida):
        with patch("builtins.input", side_effect=entradas):
            try:
                main.main()
            except SystemExit:
                pass
    texto = saida.getvalue()
    assert "Produto adicionado com sucesso!" in texto
    assert "Caneta" in texto
