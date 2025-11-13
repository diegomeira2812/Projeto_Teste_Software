# tests/unitarios/test_performance.py
import time
from unittest.mock import patch
from services.produto_service import ProdutoService

def test_performance_insercao_massiva_sem_bd():
    """Mede performance simulando 100 inserções com mock (sem acessar o BD real)."""
    with patch("services.produto_service.ProdutoService.adicionar_produto", return_value=None):
        service = ProdutoService()

        inicio = time.perf_counter()
        for i in range(100):
            service.adicionar_produto(f"Produto{i}", "Teste", 1.0, 1, 1)
        duracao = time.perf_counter() - inicio

        assert duracao < 0.5, f"Inserção simulada lenta: {duracao:.2f}s"
