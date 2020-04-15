name = input('Digite seu nome: ')
number = float(input('Digite um número: '))
double = number * 2
triple = number * 3
rq = number ** (1 / 2)
print('Olá {} seja bem-vindo! \n O número que vc digitou é {}'.format(name, number), end=' ')
print('O seu dobro é {}, o seu triplo é {} e a sua raiz quadrada é {:.2f}'.format(double, triple, rq))
