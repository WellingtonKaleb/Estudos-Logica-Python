#===== DESAFIO 013 =====
#Faca um algoritmo que leia o salario de um funcionario e mostre seu novo
#salario com 15% de aumento

salario = float(input('Digite seu salario: '))
aumento = 15
novsalario = salario * aumento / 100 + salario

print('Seu novo salario com 15% de aumento: {:.2f}'.format(novsalario))