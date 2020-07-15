# 008
# Escreva um programa que leia um valor em metros
# e o exiba convertido em centimetros e milimetros


metro = float(input('Digite um valor em metros: '))
cent = metro * 100
mili = metro * 1000

print('{} metros é igual a {:.0f} centimetros e {:.0f} milimetros.'.format(metro, cent, mili))