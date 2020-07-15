# Aula 07

# __ Operações Aritméticas
'''
Operadores Aritméticos
+  Adição 
-  Subtração
*  multiplicação
/  Divisão 
** Potencia 
// Divisão inteira 
%  Resto da divisão
'''
# Os operandos podem ser numero, strings ou até mesmo variáveis.
# Os simbolo de igualdade em programação são dois  iguais "=="
# Exemplos:
5 + 2 == 7
5 - 2 == 3
5 * 2 == 10
5 / 2 == 2.5 
5 ** 2 == 25 
5 // 2 == 2
5 % 2 == 5

Ordem de Precedência do operadores:
1º ("os parenteses")
2º ** Potencia
3º * / // % Faz quem aparece primeiro 
4º + - soma e subtração binárias 

Exemplos:
1) 
5+3*2 == 11
2)
3*5+4**2 == 31
3)
3*(5+4)**2 == 243


Exercicios:
# Eu posso fazer potencia utilizando "pow()" 
# que é uma função nativa, porem eu perdo a ordem de precedencia.

Eu posso decobri a raiz quadrada de um numero, fazendo ele elevado a meio 
Exemplo : 81**(1/2) == 9

Se eu usar : 'oi'* 5 o resultado será 'oioioioioi'
logo com isso eu posso fazer uma repetição da tela. 

Posso mexer com alinhamento tbm 
{:=^20} -> irá alinhar o texto em 20 espaços preenchidos com o = 


n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

print("A soma vale {}".format(n1+n2))

#Eu uso .format em variaveis, quando eu quero guardadar os valores.
# Exemplos
s = n1 + n2 
m = n1 * n2
d = n1 / n2 
di = n1 // n2
e = n1 ** n2 
# tem como formatar tbm o numero de casa flutuantes ex: :.3f
print('As soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira {} e potência {}'.format(di,e))

# Para quebrar a linha eu posso usar : \n.
# Para não quebrar em dois prints, eu posso usar "end=' '"

# __ Desafios 

# 005 
# Faça um programa que leia um número inteiro e
# mostre na tela o seu sucessor e seu antecessor.

# # 006 
# Crie um algoritmo que leia um número e mostre
# o seu dobro, triplo e raiz quadrada.

# 007
# Desenvolva um programa que leia as duas notas 
# de um aluno, calcule e mostre a sua média. 

# 008
# Escreva um programa que leia um valor em metros
# eo exiba convertido em centimetros e milimetros

# 009
# Faça um programa que leia um número inteiro qualquer 
# e mostre na tela a sua tabuada

# 010
# Crie um programa que leia quanto dinheiro uma pessoa
# tem na casteira e mostre quantos dólares ela pode comprar
# Obs: Considere us$ 1.00 = R$3.27

# 011
# Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta 
# necessária para pintá-la, sabendo que cada litro da tinta,
# pinta uma área de 2m².

# 012
# Faça  um algoritmo que leia o preço de um produto e mostre 
# seu novo preço, com 5% de desconto

# 013
# Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento 
