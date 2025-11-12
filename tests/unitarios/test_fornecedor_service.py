import pytest
from services.fornecedor_service import FornecedorService

@pytest.fixture
def service():
    return FornecedorService()

def test_adicionar_fornecedor_valido(service):
    service.adicionar_fornecedor("Papelaria Silva", "119999999", "12345678000100")
    fornecedores = service.listar_fornecedores()
    assert len(fornecedores) == 1
    assert fornecedores[0].nome == "Papelaria Silva"

def test_adicionar_fornecedor_invalido(service):
    with pytest.raises(ValueError):
        service.adicionar_fornecedor("", "119999999", "")
