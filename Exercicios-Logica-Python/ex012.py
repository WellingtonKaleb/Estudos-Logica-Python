#===== DESAFIO 012 =====
#Faca um algoritmo que leia o preco de um produto e mostra seu novo preco, com 5% de desconto

produto = float(input('Digite o preco a ser promocionado: '))
promocao = 5
desconto = (produto * promocao) / 100
valor = produto - desconto

print('Produto com desconto de 5%: {:.2f}'.format(valor))