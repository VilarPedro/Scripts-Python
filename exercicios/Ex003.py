# EX 003

'''
Receba dois numeros e mostre a soma entre eles 
'''
# Resposta 01
n1 = int(input("digite um numero:"))
n2 = int(input("digite outro numero:"))
s = n1+n2
print(f"A soma entre {n1} e {n2} é igual a: {s}")

# Resposta 02
resposta = 'A soma entre {0} e {1} é igual a: {2}'
print(resposta.format(n1,n2,s))
