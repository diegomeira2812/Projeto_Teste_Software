# tests/test_estrutural_branches.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from services.produto_service import ProdutoService



def test_adicionar_produto_branch_invalido():
    service = ProdutoService()
    # Branch: preço inválido
    with pytest.raises(ValueError):
        service.adicionar_produto("Item", "Teste", 0, 10, 1)

def test_atualizar_quantidade_branch_negativa():
    service = ProdutoService()
    service.adicionar_produto("Item", "Teste", 5, 10, 1)
    with pytest.raises(ValueError):
        service.atualizar_quantidade(1, -1)
