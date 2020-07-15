# 012
# Faça  um algoritmo que leia o preço de um produto e mostre 
# seu novo preço, com 5% de desconto

preco = float(input("Digite o preço do produto: "))
desconto_produto = preco*(5/100)
produto = preco - desconto_produto
print("O preço desse produto é de {}, com um desconta de 5%, fica : {:.2f}".format(preco,produto))

# OU

preco = float(input("Digite o preço do produto: "))
novo_preco = preco - (preco*(5/100))
print("O preço desse produto é de {}, com um desconta de 5%, fica : {:.2f}".format(preco,novo_preco))
