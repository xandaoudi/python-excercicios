meters = float(input('Digite o valor em metros que deseja ser convertido: '))
dm = meters * 10
cm = meters * 100
mm = meters * 1000
km = meters / 1000
hm = meters / 100
dam = meters / 10

print('O valor digitado em metros é {:.2f}, \nSua conversão para decímetro é {:.2f}'.format(meters, dm))
print('Sua conversão para centímetros é {:.2f}'.format(cm))
print('Sua conversão para milímetros é {:.2f}'.format(mm))
print('Sua conversão para quilômetros é {:.3f}'.format(km))
print('Sua conversão para hectômetros é {:.3f}'.format(hm))
print('Sua conversão para decâmetros é {:.3f}'.format(dam))
