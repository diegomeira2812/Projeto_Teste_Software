# tests/test_integracao_estoque.py
from services.produto_service import ProdutoService
from services.fornecedor_service import FornecedorService
import pytest

pytestmark = pytest.mark.integration

def test_fluxo_completo_de_cadastro_e_busca():
    fornecedor_service = FornecedorService()
    produto_service = ProdutoService()

    # 1. Adicionar fornecedor
    fornecedor_service.adicionar_fornecedor("Fornecedor ABC", "1144445555", "11111111000100")
    fornecedores = fornecedor_service.listar_fornecedores()
    assert len(fornecedores) == 1
    f_id = fornecedores[0].id

    # 2. Adicionar produto vinculado
    produto_service.adicionar_produto("Mouse", "Informática", 80.0, 20, f_id)

    # 3. Listar produtos
    produtos = produto_service.listar_produtos()
    assert len(produtos) == 1
    assert produtos[0].nome == "Mouse"

    # 4. Buscar por categoria
    encontrados = produto_service.buscar_por_categoria("Informática")
    assert len(encontrados) == 1
    assert encontrados[0].nome == "Mouse"

def test_atualizacao_e_remocao_de_produto():
    service = ProdutoService()
    service.adicionar_produto("Teclado", "Informática", 120.0, 10, 1)
    produto = service.listar_produtos()[0]

    # Atualizar
    service.atualizar_quantidade(produto.id, 15)
    atualizado = service.listar_produtos()[0]
    assert atualizado.quantidade == 15

    # Remover
    service.remover_produto(produto.id)
    produtos = service.listar_produtos()
    assert len(produtos) == 0
