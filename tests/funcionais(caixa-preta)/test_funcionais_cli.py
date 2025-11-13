# tests/test_funcionais_cli.py
import sys
import os
import io
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from services.produto_service import ProdutoService
from services.fornecedor_service import FornecedorService

pytestmark = pytest.mark.functional

def simular_input(valores):
    """Simula entradas de teclado sequenciais."""
    def mock_input(_=None):
        return valores.pop(0)
    return mock_input

def capturar_saida(func, *args, **kwargs):
    """Captura o texto impresso no console."""
    stdout = io.StringIO()
    sys_stdout = sys.stdout
    sys.stdout = stdout
    try:
        func(*args, **kwargs)
    finally:
        sys.stdout = sys_stdout
    return stdout.getvalue()

def test_adicionar_fornecedor_e_listar():
    f_service = FornecedorService()
    f_service.adicionar_fornecedor("Fornecedor Func", "11900000000", "55555555000166")
    fornecedores = f_service.listar_fornecedores()
    assert any(f.nome == "Fornecedor Func" for f in fornecedores)

def test_adicionar_produto_e_listar():
    f_service = FornecedorService()
    p_service = ProdutoService()
    f_service.adicionar_fornecedor("F Func", "11911111111", "66666666000155")
    f_id = f_service.listar_fornecedores()[0].id
    p_service.adicionar_produto("Lápis", "Papelaria", 0.5, 100, f_id)
    produtos = p_service.listar_produtos()
    assert any(prod.nome == "Lápis" for prod in produtos)