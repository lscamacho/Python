import math

angulo = float(input('Digite o valor do angulo: '))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))


print(f'O Angulo de {angulo} graus tem SENO de {sen:.2f}')
print(f'O Angulo de {angulo} graus tem COSSENO de {cos:.2f}')
print(f'O Angulo de {angulo} graus tem TANGENTE de {tan:.2f}')
