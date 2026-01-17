#===== DESAFIO 004 =====
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
#primitivo e todas as informacoes possiveis sobre ele.

algo = input('Digite algo: ')

print('o tipo primitivo desse valor e: ', type(algo))

print('So tem espaco', algo.isspace())

print('E um numero?', algo.isnumeric())

print('E tem letra?', algo.isalpha())

print('E alphanumerico?', algo.isalnum())

print('Tem letra maiuscula?', algo.isupper())

print('Tem letra minuscula?', algo.islower())

print('Esta capitalizada?', algo.istitle())

print('Tem numero decimal?', algo.isdecimal())