#===== DESAFIO 008 =====
#Escreva um programa que leia um valor em metros e
#exiba convertido em centimetros e milimetros.

mt = float(input('Digite o valor em metros a ser convertido: '))
cm = mt * 100
mm = mt * 1000

print('\n{:.2f}Mt equivale a {:.0f}Cm e {:.0f}Mm'.format(mt, cm, mm))