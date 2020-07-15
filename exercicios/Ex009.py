# 009
# Faça um programa que leia um número inteiro qualquer 
# e mostre na tela a sua tabuada

num = int(input("Digite um numero inteiro: "))
print ('-' * 15)
mult = 1 
while(mult < 11):
  print('{} x {:2} = {}\n '.format(num, mult,num*mult))
  mult += 1

print ('-' * 15)
