#===== DESAFIO 010 =====
#Crie um programa que leia quanto dinheiro uma pessoa tem
#na carteira e mostre quantos dolares ela pode comprar

din = float(input('Qual o saldo da sua carteira? R$'))
dolar = float(3.27)

print('Voce pode comprar US${:.2f} dolares.'.format(din / dolar))