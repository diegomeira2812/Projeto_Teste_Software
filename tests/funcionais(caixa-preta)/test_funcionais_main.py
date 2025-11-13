# tests/test_funcionais_main.py
import sys
import os
import io
import pytest
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from services.produto_service import ProdutoService
from services.fornecedor_service import FornecedorService

import main

pytestmark = pytest.mark.functional

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

def test_busca_por_categoria_funcional():
    f_service = FornecedorService()
    p_service = ProdutoService()
    f_service.adicionar_fornecedor("F Buscas", "11922222222", "77777777000144")
    f_id = f_service.listar_fornecedores()[0].id
    p_service.adicionar_produto("Caderno", "Papelaria", 10.0, 20, f_id)
    p_service.adicionar_produto("Borracha", "Papelaria", 1.0, 50, f_id)
    encontrados = p_service.buscar_por_categoria("Papelaria")
    assert len(encontrados) >= 2

def test_atualizar_quantidade_funcional():
    f_service = FornecedorService()
    p_service = ProdutoService()
    f_service.adicionar_fornecedor("F Atualiza", "11933333333", "88888888000133")
    f_id = f_service.listar_fornecedores()[0].id
    p_service.adicionar_produto("Apontador", "Papelaria", 2.0, 10, f_id)
    produto = p_service.listar_produtos()[0]
    p_service.atualizar_quantidade(produto.id, 25)
    atualizado = p_service.listar_produtos()[0]
    assert atualizado.quantidade == 25

def test_remover_produto_funcional():
    f_service = FornecedorService()
    p_service = ProdutoService()
    f_service.adicionar_fornecedor("F Remove", "11944444444", "99999999000122")
    f_id = f_service.listar_fornecedores()[0].id
    p_service.adicionar_produto("Tesoura", "Papelaria", 15.0, 5, f_id)
    produtos = p_service.listar_produtos()
    prod_id = produtos[0].id
    p_service.remover_produto(prod_id)
    restantes = p_service.listar_produtos()
    assert all(p.id != prod_id for p in restantes)