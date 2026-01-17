# ===== DESAFIO 009 =====
# Faca um programa que laia um numero inteiro qualquer e mostre na tela a sua tabuada.

nq = int(input('Digite um numero inteiro para saber sua tabuada: '))

print('-' * 12)

for i in range(1, 11):
    if i == 10:
        print('{} x {} = {}'.format(nq, i, nq * i))
    else:
        print('{} x {:2} = {}'.format(nq, i, nq * i))

print('-' * 12)