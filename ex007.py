name = input('Coloque seu nome: ')
test1 = float(input('Coloque a nota da primeira prova: '))
test2 = float(input('Coloque a nota da segunda prova: '))
average = (test1 + test2)/2
print('Olá {} seja bem-vindo. A nota da sua primeira prova é {:.2f}'.format(name, test1), end=' ')
print('A nota da sua segunda prova é {:.2f} e a sua média foi de {:.2f}'.format(test2, average))
