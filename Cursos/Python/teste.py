# import time

# estoque_lista = []

# estoque = [
#     {"nome": "Abacaxi", "preço": 6.50, "qtd": 20},
#     {"nome": "Café", "preço": 24.4449, "qtd": 16},
# ]

# dic = {
#     "nome": nome,
#     "preço": "valor",
# }
# estoque.append(dic)


# # print(f"{estoque[1]['preço']:.2f}")


# # def add_produto():
    
# #     nome_produto = input("Digite o nome: ")
# #     produto_no_estoque = False
# #     for produto in estoque:
# #         if nome_produto == produto['nome']:
# #             produto_no_estoque = True

# #     if produto_no_estoque:
# #         print(f"{nome_produto}, já está no estoque!")
# #     else:
# #         preco_produto = input("Digite o preço: ")
# #         qtd_produto = input("Digite a quantidade: ")
        
# #         produto = {
# #             "nome": nome_produto,
# #             "preço": preco_produto,
# #             "qtd": qtd_produto,
# #         }
# #         estoque.append(produto)
    

    





# # def add_produto():
# #     nome_produto = input("Digite o nome do produto: ").lower()
    
# #     for produto in estoque:
# #         if produto["nome"].lower() == nome_produto.lower():
# #             print(f"{nome_produto} já está no estoque!")
# #             return
# #         else:
# #             preco_produto = input("Digite o preço do produto: ")    
# #             qtd_produto = input("Digite a qauntidade do produto: ")    

# #             produto = {
# #                 "nome": nome_produto,
# #                 "preço": preco_produto,
# #                 "qtd": qtd_produto,
# #             }
# #             estoque.append(produto)
    

# # add_produto()
# # print(estoque)




















# # nome = input("Digite o nome do item: ")
# # preco = input("Digite o preço do item: ")
# # qtd = input("Digite a quantidade do item: ")

# # novo_item = {
# #     "nome": nome,
# #     "preço": preco,
# #     "qtd": qtd
# # }










# # def ver_lista(lista):
# #     print("--- Lista Atual ---")
# #     for index, item in enumerate(lista):
# #         if lista == estoque:
# #             print(f"{index:<5} | {item['nome']:<15} | {item['qtd']:<5} | R$ {item['preço']:.2f}")
# #             time.sleep(0.4)

# # ver_lista(estoque)


arquivo = open("texto.txt", "w",encoding="utf-8")
arquivo.write("Olá")
print(arquivo)