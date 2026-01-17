#===== DESAFIO 007 =====
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1 + n2) / 2
total = n1 + n2

print('\nSeu total e: {:.1f} \nSua media e: {:.1f}'.format(total, media))