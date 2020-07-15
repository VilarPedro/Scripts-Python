# Aula 08
# Trabalhando com módulos 

# Podemos fazer importações de biblíotecas em linguanges de prograções

import bebida # nesse exemplo ele irá trazer todos as bebidas 
# Todas as funcionalidades. 

from doce import pudim # Já desse modo, irá trazer somento pudim dentre todods os doces 
# apenas a funcionalidade que eu escolher

import comida 
 
 # biblioteca padrão 
# biblioteca de matemática 
math 
 ceil # arredonda para cima 
 floor # arredonda para baixa
 trunc # truncar o numero 
 pow # potencia
 sqrt # raiz quadrada
 factorial # fatorial

import math
from math import 

# Para importar mais de uma 
from math import sqrt, ceil

'''
import math
num = int(input("Digite um numero: "))
raiz = math.sqrt(num)

print('A raiz de um {} é igual a {}'.format(num, math.ceil(raiz)))
# math.ceil() para arredondar a raiz para cima 
# ou 
print('A raiz de um {} é igual a {:.2f}'.format(num,(raiz)))

# OOOUUU

from math import sqrt, floor
num = int(input("Digite um numero: "))
raiz = sqrt(num)
print('A raiz de um {} é igual a {}'.format(num,floor(raiz)))
'''
# Eu posso, eu mesmo criar a minha própria biblíoteca. 
# e todos os usuários da comunidade python podem ultilizar ela também. 
import emoji


# EXEMPLO 

import random 
num = random.random() # gera um numero aleatório entre 0 e 1
num2 = random.randint(1,10) # gera um numero aleatório entre 1 e 10 

print(num)
print(num2)

import emoji # clique com o botão direito, install package emoji 

import emoji 
print(emoji.emojize("olá, Mundo :sunglasses:", use_aliases=True))
print(emoji.emojize("olá, Mundo :earth_americas:", use_aliases=True))

#  Desafios

# 016 Crie um programa que leia um número Real qualquer pelo teclado e 
# mostre na tela a sua porção inteira
# Ex : Digite um numero: 6.127 O número 6.127 tem a parte inteira 6. 

# 017 Faça um programa que leia o comprimeito do cateto oposto e do 
# cateto adjacente de um triângulo retângulo. Calcule e mostre o 
# comprimento da hipotemusa. 

# 018 Faça um programa que leia um ângulo qualquer e mostre na tela o 
# valor do seno, cosseno e tangente desse ângulo.


