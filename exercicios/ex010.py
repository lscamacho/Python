#Programa que lê a quantidade de dinheiro em real e mostra qantos dólares se pode comprar. Cotação do dia 22/06/2021

qtd_real = float(input('Digite quanto você tem na carteira: '))

qtd_dolar = qtd_real*5.01

print(f'A quantidade de dólares que você pode comprar com R${qtd_real} é de ${qtd_dolar:.2f}')