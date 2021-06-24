#Faça um programa que leia um número e mostra a sua tabuada

num = int(input('Digite um número:\n'))
print(f'A tabuada de {num} é:')

for i in range (10):
    result = num*i
    print(f'{num} * {i} = {result}')