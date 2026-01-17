#===== DESAFIO 005 =====
#Faça um programa que leia um numero inteiro e mostre na tela
#o seu sucessor e o seu antecessor.

n = int(input('Digite um numero: '))

print('\nO numero e: {} \nSeu antecessor e: {}'
'\nSeu sucessor e: {}'.format(n, (n-1), (n+1)))