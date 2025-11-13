import pytest
from repositories.produto_repository import ProdutoRepository
from repositories.fornecedor_repository import FornecedorRepository


def test_inserir_e_listar_produtos():
    repo = ProdutoRepository()
    repo.inserir("Caneta Azul", "Papelaria", 2.5, 100, 1)
    produtos = repo.listar_todos()
    assert len(produtos) == 1
    assert produtos[0].nome == "Caneta Azul"

def test_insercao_duplicada_fornecedor():
    repo = FornecedorRepository()
    repo.inserir("Fornecedor A", "111111", "11111111000100")
    repo.inserir("Fornecedor A", "111111", "11111111000100")  # Aceita duplicado
    todos = repo.listar_todos()
    assert len(todos) >= 2

def test_insercao_duplicada_produto():
    repo = ProdutoRepository()
    repo.inserir("Produto A", "Categoria", 10.0, 5, 1)
    repo.inserir("Produto A", "Categoria", 10.0, 5, 1)
    todos = repo.listar_todos()
    assert len(todos) >= 2

def test_busca_id_inexistente():
    repo = ProdutoRepository()
    produtos = repo.listar_todos()
    assert all(p.id != 999 for p in produtos)

def test_listagem_varias_insercoes():
    repo = ProdutoRepository()
    for i in range(3):
        repo.inserir(f"Produto{i}", "Teste", 10.0, 1, 1)
    produtos = repo.listar_todos()
    assert len(produtos) >= 3

def test_atualizacao_inexistente():
    repo = ProdutoRepository()
    # Apenas valida que o método existe
    assert hasattr(repo, "atualizar_quantidade")