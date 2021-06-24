#Fazendo a leitura do dado
dado = input('Entre com a informação: ')

#Mostrando algumas informações do dado digitado
print('O tipo primitivo desse dado é: ',type(dado))
print('Só tem espaços?',dado.isspace())
print('É um numérico?', dado.isnumeric())
print('É alfabético?', dado.isalpha())
print('É alfanumerico', dado.isalnum())
print('Está em maiúsculas?', dado.isupper())
print('Está em minusculas?',dado.islower())
print('Está captalizada?', dado.istitle())
