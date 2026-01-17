#===== DESAFIO 011 =====
#Faca um programa que leia a largura e a altura de uma parede em metros, calcula
#a dua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro
#de tinta, pinta uma area de 2m^2

largura = float(input('Digite a largura da parede em Metros: '))
altura = float(input('Digite a altura da parede em Metros: '))

area = largura * altura
tinNec = area / 2

print('\nA area da parede e: {:.2f}m² e serao necessarios {:.2f} litros de tintas para pinta-la'.format(area, tinNec))