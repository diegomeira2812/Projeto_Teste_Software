from repositories.fornecedor_repository import FornecedorRepository
from utils.logger import get_logger

logger = get_logger()

class FornecedorService:
# servico responsavel pelas regras de negocio dos fornecedores

    def __init__(self):
        self.repo = FornecedorRepository()

    def listar_fornecedores(self):
        return self.repo.listar_todos()

    def adicionar_fornecedor(self, nome: str, contato: str, cnpj: str):
        if not nome or not cnpj:
            raise ValueError("Nome e CNPJ são obrigatórios.")
        self.repo.inserir(nome, contato, cnpj)
        logger.info(f"Fornecedor '{nome}' cadastrado com sucesso.")
