from repositories.produto_repository import ProdutoRepository

def test_inserir_e_listar_produtos():
    repo = ProdutoRepository()
    repo.inserir("Caneta Azul", "Papelaria", 2.5, 100, 1)
    produtos = repo.listar_todos()
    assert len(produtos) == 1
    assert produtos[0].nome == "Caneta Azul"
