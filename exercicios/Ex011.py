# 011
# Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta 
# necessária para pintá-la, sabendo que cada litro da tinta,
# pinta uma área de 2m².

largura = float(input('Digite a lagura da sua parece: '))
altura = float(input('Digite a altura da sua parece: '))

area = largura * altura

litros = area / 2

print('A dimensão da sua parede é de {}x{},5 sua área é de {:.1f}m² e,\nvocê precisa de {:.1f}L de tinta para pinta-la.'.format(largura,altura,area, litros))
