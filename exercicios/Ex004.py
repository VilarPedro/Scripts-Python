'''
 04) Faça um programa que leia algo pelo teclado e mostre na tela o seu 
 tipo primitivo e todas as informações possiveis sobre ela. 
'''
# n = 'pedro'
# print()

var = input('Digite algo: ')
print('O que você digitou pode ser um numero:',var.isnumeric())
print('O que você digitou pode ser uma string:',var.isalpha())
# print('O que você digitou pode ser um numero:',var.isnumeric())
# print('O que você digitou pode ser um numero:',var.isnumeric())
# print('O que você digitou pode ser um numero:',var.is())
# n = 'pedro'
# print(n.is)

# __ Solução do guanabara 

# a função input sempre irá retornar um tipo str.
a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
# Verifica se tem somente espaços 
print('Só tem espaços? ', a.isspace())
# verificar se só é numerico 
print('é um numero? ', a.isnumeric())
# verificar se só é alfabético
print('é alfabético? ', a.isalpha())

print('é alfanumérico? ', a.isalnum())
print('está em maiúsculo? ', a.isupper())
print('está em minúscula? ', a.islower())
print('está capitalizada? ', a.istitle())


# isalnum
# isalpha
# isnumeric
# isspace
# isprintable
# isdecimal
# istitle
# islower
# isupper
# isdigit

# Todo obejeto tem caracteristicas e possui funcionalidades, atributos e metodos.

# Todos os métodos da string
'''
Método	    Parâmetros  Descrição

upper	    nenhum	    Retorna um string todo em maiúsculas
lower	    nenhum	    Retorna um string todo em minúsculas
capitalize	nenhum	    Retorna um string com o primeiro caractere em maiúscula, e o resto em minúsculas
strip	    nenhum  	Retorna um string removendo caracteres em branco do início e do fim
lstrip	    nenhum	    Retorna um string removendo caracteres em brando do início
rstrip	    nenhum	    Retorna um string removendo caracteres em brando do fim
count	    item	    Retorna o número de ocorrências de item
replace	    old, new	Substitui todas as ocorrências do substring old por new
center	    largura	    Retorna um string centrado em um campo de tamanho largura
ljust	    largura	    Retorna um string justificado à esquerda em um campo de tamanho largura
rjust	    largura	    Retorna um string justificado à direita em um campo de tamanho largura
find	    item	    Retorna o índice mais à esquerda onde o substring item é encontrado
rfind	    item	    Retorna o índice mais à direita onde o substring item é encontrado
index	    item	    Como find, mas causa um erro em tempo de execução caso item não seja encontrado
rindex	    item	    Como rfind, mas causa um erro em tempo de execução caso item não seja encontrado

'''
