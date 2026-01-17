#===== DESAFIO 016 =====
#Crie im programa que leia um numero real qualquer pelo teclado e mostre
#na tela a sua porcao inteira. Ex: num 6.127, porc.int 6
from math import trunc

num = float(input('Digite um numero: '))

print('O numero {} tem a parte inteira {}'.format(num, trunc(num)))