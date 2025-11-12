# tests/test_integracao_valor_total.py
from services.produto_service import ProdutoService

def test_calculo_valor_total_com_integração():
    service = ProdutoService()
    service.adicionar_produto("Monitor", "Informática", 1000.0, 5, 1)
    service.adicionar_produto("HD Externo", "Informática", 400.0, 10, 1)

    total = service.calcular_valor_total()
    assert total == 1000.0 * 5 + 400.0 * 10  # 9000
