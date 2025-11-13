# tests/unitarios/test_produto_service_mock.py
def test_adicionar_produto_mockado(mocker):
    """Verifica se o método de inserção é chamado corretamente sem tocar no BD."""
    mock_repo = mocker.patch("services.produto_service.ProdutoRepository")
    instance = mock_repo.return_value

    from services.produto_service import ProdutoService
    service = ProdutoService()
    service.adicionar_produto("Caderno", "Papelaria", 10.0, 5, 1)

    instance.inserir.assert_called_once_with("Caderno", "Papelaria", 10.0, 5, 1)


def test_calcular_valor_total_mockado(mocker):
    """Valida o cálculo de valor total simulando produtos mockados."""
    mock_repo = mocker.patch("services.produto_service.ProdutoRepository")
    instance = mock_repo.return_value

    # Simula dois produtos retornados
    instance.listar_todos.return_value = [
        type("Produto", (), {"preco": 10, "quantidade": 5}),
        type("Produto", (), {"preco": 20, "quantidade": 3}),
    ]

    from services.produto_service import ProdutoService
    service = ProdutoService()
    total = service.calcular_valor_total()

    assert total == 110, f"Esperado 110, mas retornou {total}"
