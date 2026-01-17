#===== DESAFIO 015 =====
#Escreva um programa que pergunte a quantidade de Km percorrido por um carro
#alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a
#pagar, sabendo que o carro custa R$60 por dia e R$0,15 po Km rodado.

dias = int(input('Dias alugados: '))
km = float(input('Km rodados: '))

cd = dias * 60
ckm = km * 0.15

pago = (dias * 60) + (km * 0.15)

print('O total a pagar e de R${:.2f}'.format((dias * 60) + (km * 0.15)))