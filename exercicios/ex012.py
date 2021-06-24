#Programa para ler o preço de um produto dar um desconto de 5%

preco_produto = float(input('Digite o preço do produto\n'))

preco_desconto = preco_produto * 0.95

print(f'O preco do produto com 5% de desconto é\nR${preco_desconto:.2f}')