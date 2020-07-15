# 013
# Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento 

salario = float(input("Digite o valor do seu salário: "))
aumento = salario *(15/100)
novo_salario = salario + aumento
print("Seu salário é {:.2}, com um aumento de 15%, ficará: {:.2}".format(salario,novo_salario))

# Ou

salario = float(input("Digite o valor do seu salário: "))
aumento = salario + (salario *(15/100))
print("Seu salário é {:.2}, com um aumento de 15%, ficará: {:.2}".format(salario,aumento))
