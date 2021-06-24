#Leia um numero e mostre eu dobro, seu triplo e sua raiz quadrada

num = int(input('Digite um número: '))

dobro = num*2
triplo = num*3
raiz = num**(1/2)

print(f'O dobro de {num} é = {dobro}\nO triplo de {num} é = {triplo}\nA raiz quadradad de {num} é = {raiz:.2f}')