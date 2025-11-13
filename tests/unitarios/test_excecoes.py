import pytest
from services.produto_service import ProdutoService

def test_excecao_fornecedor_inexistente():
    """Verifica se o sistema lida com fornecedor inexistente sem quebrar."""
    service = ProdutoService()

    try:
        service.adicionar_produto("ProdutoZ", "Categoria", 10.0, 5, 9999)
    except Exception as e:
        pytest.fail(f"Erro inesperado: {e}")

def test_excecao_preco_invalido():
    """Verifica se produtos com preço inválido são rejeitados."""
    service = ProdutoService()
    with pytest.raises(ValueError):
        service.adicionar_produto("ProdutoY", "Categoria", 0, 5, 1)
