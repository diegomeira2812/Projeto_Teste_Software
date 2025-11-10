from dataclasses import dataclass

@dataclass
class Produto:
# representa um produto no estoque
    id: int
    nome: str
    categoria: str
    preco: float
    quantidade: int
    fornecedor_id: int | None
