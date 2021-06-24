#Programa para ler um numero real e mostrar sua parte inteira
from math import trunc
num = float(input('Digite um número: '))

print(f'O numero {num} tem a parte inteira {trunc(num)}')