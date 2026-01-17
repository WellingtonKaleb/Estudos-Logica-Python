#===== DESAFIO 014 =====
#Escreva um programa que converte uma temperatura digitada em C e cenverta para F

c = float(input('Digite sua temperatura atual: '))
f = c * 1.8 + 32 #O meu jeito de responder
#f = 9 * c / 5 + 32

print('A temperatura de {}C corresponde a {}F'.format(c, f))