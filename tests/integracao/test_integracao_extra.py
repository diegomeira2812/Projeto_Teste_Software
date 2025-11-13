# tests/test_integracao_extra.py
import pytest
from services.fornecedor_service import FornecedorService
from services.produto_service import ProdutoService
from utils.db_connection import get_connection

pytestmark = pytest.mark.integration

def test_fornecedor_persistencia_db():
    f_service = FornecedorService()
    f_service.adicionar_fornecedor("Fornecedor XYZ", "1199998888", "22222222000199")
    with get_connection() as conn:
        cur = conn.execute("SELECT COUNT(*) FROM fornecedores")
        count = cur.fetchone()[0]
    assert count == 1

def test_produto_vinculado_e_persistencia_db():
    f_service = FornecedorService()
    p_service = ProdutoService()
    f_service.adicionar_fornecedor("Fornecedor Link", "1188887777", "33333333000188")
    f = f_service.listar_fornecedores()[0]
    p_service.adicionar_produto("Webcam", "Informática", 150.0, 25, f.id)
    with get_connection() as conn:
        cur = conn.execute("SELECT fornecedor_id FROM produtos WHERE nome = ?", ("Webcam",))
        row = cur.fetchone()
    assert row is not None
    assert row[0] == f.id

def test_busca_por_categoria_varios():
    f_service = FornecedorService()
    p_service = ProdutoService()
    f_service.adicionar_fornecedor("F1", "1100001111", "44444444000177")
    f_id = f_service.listar_fornecedores()[0].id
    p_service.adicionar_produto("Produto A", "Informática", 10.0, 5, f_id)
    p_service.adicionar_produto("Produto B", "Escritório", 20.0, 3, f_id)
    p_service.adicionar_produto("Produto C", "Informática", 5.0, 10, f_id)

    encontrados = p_service.buscar_por_categoria("Informática")
    nomes = {p.nome for p in encontrados}
    assert len(encontrados) == 2
    assert nomes == {"Produto A", "Produto C"}

def test_atualizacao_quantidade_sequencial():
    p_service = ProdutoService()
    # pressupõe fornecedor id 1 existir ou não ser exigido; se exigir, crie um fornecedor antes
    p_service.adicionar_produto("Cabo USB", "Informática", 8.0, 20, 1)
    produto = p_service.listar_produtos()[0]
    p_service.atualizar_quantidade(produto.id, 8)
    p_service.atualizar_quantidade(produto.id, 3)
    atualizado = p_service.listar_produtos()[0]
    assert atualizado.quantidade == 3

def test_calculo_valor_total_com_varios_produtos():
    p_service = ProdutoService()
    p_service.adicionar_produto("SSD", "Informática", 300.0, 2, 1)
    p_service.adicionar_produto("Fonte", "Informática", 250.0, 1, 1)
    total = p_service.calcular_valor_total()
    assert total == 300.0 * 2 + 250.0 * 1

def test_remocao_e_consistencia_pos_remocao():
    p_service = ProdutoService()
    p_service.adicionar_produto("Item X", "Geral", 50.0, 5, 1)
    p_service.adicionar_produto("Item Y", "Geral", 60.0, 2, 1)
    produtos = p_service.listar_produtos()
    assert len(produtos) >= 2
    # remove o primeiro e verifica consistência
    p_service.remover_produto(produtos[0].id)
    restantes = p_service.listar_produtos()
    assert all(p.id != produtos[0].id for p in restantes)