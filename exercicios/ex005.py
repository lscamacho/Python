#Faça um programa que leia um número inteiro e mostre na tela seu sucessor e antecessor

num = int(input('Digite um numero: '))

ant = num - 1
pos = num + 1

print(f'O antecessor de <{num}> é <{ant}> e o sucessor é <{pos}> ')