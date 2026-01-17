#===== DESAFIO 006 =====
#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um numero: '))
pow(n, (1/2))
raiz = n ** (1/2)

print('\nO numero e: {} \nSeu dobro e: {}'
'\nSeu triplo e: {} \nSua raiz quadrada e: {:.2f}'.format(n, (n*2), (n*3), raiz))