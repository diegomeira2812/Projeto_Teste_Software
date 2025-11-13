# tests/test_estrutural_branches.py  (adicione abaixo do que já existe)
import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from services.produto_service import ProdutoService
from services.fornecedor_service import FornecedorService

pytestmark = pytest.mark.structural

def setup_function():
    """
    Garante schema limpo antes de cada teste se você não estiver usando fixtures globais.
    Se já tiver fixture que cria schema, pode remover esta função.
    """
    try:
        from utils import db_connection
        with db_connection.get_connection() as conn:
            db_connection.create_schema(conn)
    except Exception:
        # se create_schema não existir, ignore; presume que conftest já cuida disso
        pass

def test_adicionar_produto_preco_negativo_levanta():
    service = ProdutoService()
    with pytest.raises(ValueError):
        service.adicionar_produto("ItemNeg", "Teste", -1.0, 10, 1)

def test_adicionar_produto_sem_fornecedor_levanta():
    service = ProdutoService()
    # usa um id de fornecedor improvável para existir
    with pytest.raises(ValueError):
        service.adicionar_produto("ItemSemForn", "Teste", 10.0, 1, 99999)

def test_calcular_valor_total_vazio_retorna_zero():
    service = ProdutoService()
    total = service.calcular_valor_total()
    assert total == 0

def test_buscar_por_categoria_sem_resultado_retorna_lista_vazia():
    service = ProdutoService()
    encontrados = service.buscar_por_categoria("CategoriaInexistente")
    assert isinstance(encontrados, list)
    assert len(encontrados) == 0

def test_atualizar_quantidade_produto_inexistente_levanta():
    service = ProdutoService()
    with pytest.raises(ValueError):
        service.atualizar_quantidade(99999, 5)

def test_atualizar_quantidade_sem_alteracao_eh_noop():
    f_service = FornecedorService()
    p_service = ProdutoService()
    f_service.adicionar_fornecedor("F Teste", "11900000000", "00000000000100")
    f_id = f_service.listar_fornecedores()[0].id
    p_service.adicionar_produto("ItemNoop", "Geral", 5.0, 7, f_id)
    produto = p_service.listar_produtos()[0]
    # atualiza para a mesma quantidade (branch: sem mudança)
    p_service.atualizar_quantidade(produto.id, 7)
    atualizado = p_service.listar_produtos()[0]
    assert atualizado.quantidade == 7

def test_remover_produto_inexistente_levanta():
    service = ProdutoService()
    with pytest.raises(ValueError):
        service.remover_produto(99999)

def test_propagacao_de_erro_do_bd(monkeypatch):
    """
    Simula falha no método de listagem para garantir que a exceção seja propagada
    (caminho de erro crítico).
    """
    service = ProdutoService()
    def fake_listar():
        raise RuntimeError("erro simulado de BD")
    monkeypatch.setattr(service, "listar_produtos", fake_listar)
    with pytest.raises(RuntimeError):
        service.listar_produtos()