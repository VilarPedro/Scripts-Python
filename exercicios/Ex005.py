# 005 
# Faça um programa que leia um número inteiro e
# mostre na tela o seu sucessor e seu antecessor.


n1 = int(input('Digite um número inteiro '))
ant = n1 - 1
suc = n1 + 1

print('O antecessor de {0} é {1}, e o sucessor é {2}'.format(n1, ant, suc))


# OU

n2 = int(input('Digite um número inteiro ')) 
print('O antecessor de {0} é {1}, e o sucessor é {2}'.format(n2, (n2-1), (n2+1)))
