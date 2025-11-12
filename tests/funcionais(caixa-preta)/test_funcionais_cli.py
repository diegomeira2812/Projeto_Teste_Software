# tests/test_funcionais_cli.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from services.produto_service import ProdutoService
from services.fornecedor_service import FornecedorService


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
