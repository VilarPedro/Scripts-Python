# 014
# Escreva um programa que coverta uma temperatura
# digitado em °C e converta para °F
# Exemplo : (31.5 °C × 9/5) + 32 = 88,7 °F

# celsius
c = float(input('Digite um temperatura em °C (Celsius): '))
# fahrenheit
f = (c * 9/5) + 32

print('A temperatura de {:.1f} °C (Celsius) correponde a {:.1f} °F (Fahrenheit).'.format(c,f))
