
from repositories.produto_repository import ProdutoRepository
from utils.logger import get_logger

logger = get_logger()

class ProdutoService:
# servico responsavel pelas regras de negocio relacionadas a produtos

    def __init__(self):
        self.repo = ProdutoRepository()

    def listar_produtos(self):
        return self.repo.listar_todos()

    def adicionar_produto(self, nome: str, categoria: str, preco: float, quantidade: int, fornecedor_id: int):
        if preco <= 0 or quantidade < 0:
            logger.warning("Tentativa de adicionar produto com valores inválidos.")
            raise ValueError("Preço e quantidade devem ser positivos.")
        self.repo.inserir(nome, categoria, preco, quantidade, fornecedor_id)
        logger.info(f"Produto '{nome}' adicionado com sucesso.")

    def atualizar_quantidade(self, produto_id: int, nova_qtd: int):
        if nova_qtd < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        self.repo.atualizar_quantidade(produto_id, nova_qtd)
        logger.info(f"Produto {produto_id} atualizado com nova quantidade: {nova_qtd}")

    def remover_produto(self, produto_id: int):
        self.repo.remover(produto_id)
        logger.info(f"Produto {produto_id} removido do sistema.")

    def buscar_por_categoria(self, categoria: str):
        return self.repo.buscar_por_categoria(categoria)

    def calcular_valor_total(self) -> float:
        produtos = self.repo.listar_todos()
        total = sum(p.preco * p.quantidade for p in produtos)
        logger.info(f"Valor total do estoque calculado: R$ {total:.2f}")
        return total
