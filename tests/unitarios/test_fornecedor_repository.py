from repositories.fornecedor_repository import FornecedorRepository

def test_inserir_e_listar_fornecedores():
    repo = FornecedorRepository()
    repo.inserir("Fornecedor XPTO", "1144445555", "12345678000100")
    fornecedores = repo.listar_todos()
    assert len(fornecedores) == 1
    assert fornecedores[0].nome == "Fornecedor XPTO"
