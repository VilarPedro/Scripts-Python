# # 006 
# Crie um algoritmo que leia um número e mostre
# o seu dobro, triplo e raiz quadrada.


num = int(input('Digite um número: '))

dobro = num * 2
triplo = num * 3
raiz = num**(1/2) 

print('O dobro de {0} é {1}, o triplo é {2} e a raiz quadrada {3} !'.format(num, dobro, triplo, raiz))

#OU

num2 = int(input('Digite um número: '))
print('O dobro de {0} é {1}, o triplo é {2} e a raiz quadrada {3} !'.format(num2, (num2 * 2), (num2 * 3), pow(num2,(1/2))))

