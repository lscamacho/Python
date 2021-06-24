#Programa que calcula a área de uma parede e mosrea quando litros de tinta é necessáeio para pinta-lá

largura = float(input('Digite a largura da parede:\n'))
altura = float(input('Digite a altura da parede:\n'))

area = largura*altura
tinta = area/2

print(f'A parede tem {area}M2 e é necessário {tinta} litros de tinta para pinta-lá')