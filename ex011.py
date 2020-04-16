height = float(input('Digite a altura da parede em metros: '))
width = float(input('Digite a largura da parede em metros: '))
area = height * width
liters = area / 2
print('A área da parede que vc deseja pintar é {:.3f} e você irá precisar de {:.3f} litros para pintá-la'.format(area, liters))
