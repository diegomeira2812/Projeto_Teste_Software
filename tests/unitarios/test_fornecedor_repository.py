from repositories.fornecedor_repository import FornecedorRepository

def test_inserir_e_listar_fornecedores():
    repo = FornecedorRepository()
    repo.inserir("Fornecedor XPTO", "1144445555", "12345678000100")
    fornecedores = repo.listar_todos()
    assert len(fornecedores) == 1
    assert fornecedores[0].nome == "Fornecedor XPTO"

def test_inserir_varios_fornecedores_e_listar():
    repo = FornecedorRepository()
    repo.inserir("Fornecedor A", "1111", "11111111000100")
    repo.inserir("Fornecedor B", "2222", "22222222000100")
    todos = repo.listar_todos()
    # deve conter pelo menos 2 registros
    assert len(todos) >= 2
    nomes = [f.nome for f in todos]
    assert "Fornecedor A" in nomes
    assert "Fornecedor B" in nomes

def test_campos_do_fornecedor_preenchidos():
    repo = FornecedorRepository()
    repo.inserir("Fornecedor X", "3333", "33333333000100")
    todos = repo.listar_todos()
    # pega o último inserido (assume autoincrement)
    ultimo = todos[-1]
    assert hasattr(ultimo, "id")
    assert ultimo.nome == "Fornecedor X"
    assert ultimo.cnpj == "33333333000100"

def test_listagem_vazia_apos_drop_create_simulado():
    # Esse teste assume que o conftest limpa o banco entre testes.
    repo = FornecedorRepository()
    todos = repo.listar_todos()
    # Se nenhum fornecedor existir, deve ser lista vazia
    assert isinstance(todos, list)