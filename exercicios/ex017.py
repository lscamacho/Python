 #Faça um programa que 
 #leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
 #Calcule e mostre o comprimento da hipotenusa.
import math

ca = float(input('Digite o valor do cateto adjacente'))
co = float(input('Digite o valor do cateto oposto'))

hp = (math.pow(ca,2)) + (math.pow(co,2))

result = math.sqrt(hp)

print(result)