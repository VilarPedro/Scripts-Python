# Aula 04

# __ Primeiros comando de python

# Mostrar coisas para os usuários

print('Olá munto')

# Mensagens tem delimitadores, que no caso são as aspas "", toda mensagem devem estar entre aspas 
# Já os numeros não tem delimitadores 

# Tem horas que a virgula será mais eficiente que o +

print(7+4)

# __ Uso de Variaveis

# utilizar sempre letras minusculas
# Em python toda variável é um objeto

nome = "Pedro" # string 
idade = 21 # int
peso = 70.2 # float

# print é um função
print (nome,idade,peso)

# input é um função

nome = input("Qual é o seu nome ?") 
idade = input("Quantos anos voce tem ?")
peso = input("Qual é o seu peso ?")

# todo arquivo de python tem a extenção .py 

# __ Desafios

'''
Crie um script python que leia o nome de uma pessoa e
mostra uma mensagem de boas-vindas de acordo com o 
valor digitado.
'''
nome = input("Olá, qual é o seu nome ?")
print("Olá",nome,"! Prazer em te conhecer!")

'''
Crie um script python que leia o dia, o mês eo ano de
nascimento de uma pessoa e mostre a mensagem com a data formatada 
'''
dia = input("Olá, qual dia do seu aniversário ?")
mes = input("Qual mês do seu aniversário ?")
ano = input("em que ano você nasceu ?")
print(f"Você nasceu no dia {dia} de {mes} de {ano} correto ?")

'''
Receba dois numeros e mostre a soma entre eles 
'''
# Resposta 01
n1 = int(input("digite um numero:"))
n2 = int(input("digite outro numero:"))
s = n1+n2
print(f"A soma de {n1} mais {n2} é igual a: {s}")

# Resposta 02
resposta = 'A soma de {0} mais {1} é igual a: {2}'
print(resposta.format(n1,n2,s))
