'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias 
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

dias_alugado = int(input('Quantos dias o carro ficou alugado? '))
km_percorridos = float(input('Quantos km o carro percorreu? '))

valor = (km_percorridos * 0.15) + (dias_alugado * 60)

print(f'O custo total foi de R${valor:.2f}')