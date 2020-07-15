# Aula 06

# __ Tipos primitivos 

# variável é um espaço na memória do computador

# __ Os 4 principais tipos primitivos são:

# 1 int,  que são tipo de numeros inteiros
# Exmplos: 7, -4, 0, 9875

# 2 float, que são numeros reais, ou numero com ponto flutuante 
# Exemplo: 4.5, 0.076, -15.223, 7.0 

# 3 bool, que recebendo valores lógicos ou boleanos
# Exemplo : valores boleanos (True, False) 

# 4 str, que recebem caractéris ou strings 
# Exemplo:  valores entre aspas, 'olá', '7.5', ''

# __Forma diferente de escrever o print :


print('As soma vale',s)

print('A soma vale {}'.format(s))

# Para se testar o tipo primitivo de um variável, se usa a função type(), 
# que retorn o tipo primitivo de um variável.

Exemplo :
n1 = input("digite um numero:")
print(type(n1)) # irá retornar um valor do tipo str 

n1 = int(input("digite um numero:"))
print(type(n1)) # irá retornar um valor do tipo int

n1 = float(input("digite um numero:"))
print(type(n1)) # irá retornar um valor do tipo float

n1 = bool(input("digite um numero:"))
print(type(n1)) # irá retornar um valor do tipo booleano (True, False)


# ".isnumeric" irá testar se o valor que esta recebendo pode se tranformar
#  em um valor numérico, retonarno True ou False. 

# ".isalpha" verificar se é letra

# __ Desafios

# 03 Crie um programs que leia dois números e mostre a soma entre eles

# 04 Faça um programa que leia algo pelo teclado e mostre na tela o seu 
# tipo primitivo e todas as informações possiveis sobre ela 
