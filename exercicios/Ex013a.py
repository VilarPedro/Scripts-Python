# 013a
# Faça um algoritmo que leia o preço de protudo,
# mostre um desconto de 5% se for pago avista 
# e um aumento de 8% se for pago a prazo   

produto = float(input("Digite o preço do produto R$: "))
avista = produto - (produto * 5/100)
prazo = produto + (produto * 8/100)

print('Pagando avisa esse produto sai de R${:.2f} por R${:.2f}, com desconto de 5%.'.format(produto, avista))
print('Se for pago parcelado ele sai de R${:.2f} por R${:.2f}, com um aumento de 8%.'.format(produto, prazo))
