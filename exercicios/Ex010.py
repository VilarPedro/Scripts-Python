# 010
# Crie um programa que leia quanto dinheiro uma pessoa
# tem na casteira e mostre quantos dólares ela pode comprar
# Obs: Considere us$ 1.00 = R$3.27

real = float(input('Digite quanto dinheiro você tem na carteira: '))
dolar = real / 5.06
euro = real / 5.68
franco_suico = real / 5.27
bitcoin = real / 48960.57
peso_argentino = real / 0.074

print('-'*12)
print('Com R$ {:.2f} da sua carteira. Você pode comparar: \n U$ {:.2f} dólares, \n €$ {:.2f} Euros, \n Fr$ {:.2f} Franco Suiço, \n ₿$ {:.2f} Bitcoin e\n $ {:.2f} Peso Argentino.'.format(real, dolar, euro, franco_suico, bitcoin, peso_argentino))
print('-'*12)
