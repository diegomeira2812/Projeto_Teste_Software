import pytest
from services.produto_service import ProdutoService

@pytest.fixture
def service():
    return ProdutoService()

def test_adicionar_produto_valido(service):
    service.adicionar_produto("Caneta", "Papelaria", 2.5, 100, 1)
    produtos = service.listar_produtos()
    assert len(produtos) == 1
    assert produtos[0].nome == "Caneta"

def test_adicionar_produto_invalido(service):
    with pytest.raises(ValueError):
        service.adicionar_produto("Borracha", "Papelaria", -5, 10, 1)

def test_atualizar_quantidade(service):
    service.adicionar_produto("Caderno", "Papelaria", 10.0, 50, 1)
    produto = service.listar_produtos()[0]
    service.atualizar_quantidade(produto.id, 80)
    atualizado = service.listar_produtos()[0]
    assert atualizado.quantidade == 80

def test_calcular_valor_total(service):
    service.adicionar_produto("Lápis", "Papelaria", 1.5, 200, 1)
    service.adicionar_produto("Caneta", "Papelaria", 3.0, 100, 1)
    total = service.calcular_valor_total()
    assert total == pytest.approx(600.0)
