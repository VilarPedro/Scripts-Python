# 015
# Escreva um programa que pergunte a quantidade de Km
# percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$60 por dia e R$0.15 por Km rodado.

dias = int(input('Por quantos dias você alugou o carro: '))
km = float(input('Quantod Km você rodou com o carro: '))

valor_dias = dias * 60
# print(valor_dias)
valor_km = km * 0.15
# print(valor_km)
total = valor_dias + valor_km
print('Você deve pagar R${:.2f}, por esse aluguel.'.format(total))
