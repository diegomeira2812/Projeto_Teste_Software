import sys
from services.produto_service import ProdutoService
from services.fornecedor_service import FornecedorService
from utils.logger import configurar_logger
from utils.config_loader import carregar_config

def menu_principal():
    print("\n--- StockMaster ---")
    print("1. Gerenciar Produtos")
    print("2. Gerenciar Fornecedores")
    print("3. Relatórios")
    print("4. Adicionar Fornecedor")
    print("0. Sair")

def menu_produtos():
    print("\n--- PRODUTOS ---")
    print("1. Listar produtos")
    print("2. Adicionar produto")
    print("3. Atualizar produto")
    print("4. Remover produto")
    print("5. Buscar por categoria")
    print("0. Voltar")

def main():
    config = carregar_config()
    logger = configurar_logger(config.get("log_file", "stockmaster.log"))

    produto_service = ProdutoService()
    fornecedor_service = FornecedorService()

    while True:
        menu_principal()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            while True:
                menu_produtos()
                sub = input("Escolha uma opção: ")

                if sub == "1":
                    produtos = produto_service.listar_produtos()
                    for p in produtos:
                        print(f"{p.id} - {p.nome} | {p.categoria} | {p.quantidade} unid.")
                elif sub == "2":
                    nome = input("Nome: ")
                    categoria = input("Categoria: ")
                    preco = float(input("Preço: "))
                    quantidade = int(input("Quantidade: "))
                    fornecedor_id = int(input("ID do fornecedor: "))
                    produto_service.adicionar_produto(nome, categoria, preco, quantidade, fornecedor_id)
                    print("Produto adicionado com sucesso!")
                elif sub == "3":
                    pid = int(input("ID do produto: "))
                    novo_qtd = int(input("Nova quantidade: "))
                    produto_service.atualizar_quantidade(pid, novo_qtd)
                    print("Produto atualizado!")
                elif sub == "4":
                    pid = int(input("ID do produto: "))
                    produto_service.remover_produto(pid)
                    print("Produto removido!")
                elif sub == "5":
                    cat = input("Categoria: ")
                    produtos = produto_service.buscar_por_categoria(cat)
                    for p in produtos:
                        print(f"{p.id} - {p.nome} | {p.quantidade} unid.")
                elif sub == "0":
                    break
                else:
                    print("Opção inválida!")

        elif opcao == "2":
            print("\n--- FORNECEDORES ---")
            fornecedores = fornecedor_service.listar_fornecedores()
            for f in fornecedores:
                print(f"{f.id} - {f.nome} | {f.contato}")

        elif opcao == "3":
            total = produto_service.calcular_valor_total()
            print(f"Valor total do estoque: R$ {total:.2f}")         


        elif opcao == "0":
            print("Saindo do sistema...")
            sys.exit()
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
