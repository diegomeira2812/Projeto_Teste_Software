from dataclasses import dataclass

@dataclass
class Fornecedor:
# representa um fornecedor do sistema
    id: int
    nome: str
    contato: str | None
    cnpj: str
