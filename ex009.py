'''
number = int(input('Qual número você deseja saber a tabuada? '))
n1 = number * 1
n2 = number * 2
n3 = number * 3
n4 = number * 4
n5 = number * 5
n6 = number * 6
n7 = number * 7
n8 = number * 8
n9 = number * 9
n10 = number * 10
print('-' * 20)
print('A tabuada de {} é:\n{} x 1  = {:2} \n{} x 2 = {:2}'.format(number, number, n1, number, n2))
print('{} x 3 = {:2} \n{} x 4 = {:2} \n{} x 5 = {:2} \n{} x 6 = {:2}'.format(number, n3, number, n4, number, n5, number, n6))
print('{} x 7 = {:2} \n{} x 8 = {:2} \n{} x 9 = {:2} \n{} x 10 = {:2}'.format(number, n7, number, n8, number, n9, number, n10))
print('-' * 20)
'''

number = int(input('Qual o númeor você deseja saber a tabuada? '))
print('-' * 12)
print('{} x {:2} = {:2}'.format(number, 1, number*1))
print('{} x {:2} = {:2}'.format(number, 2, number*2))
print('{} x {:2} = {:2}'.format(number, 3, number*3))
print('{} x {:2} = {:2}'.format(number, 4, number*4))
print('{} x {:2} = {:2}'.format(number, 5, number*5))
print('{} x {:2} = {:2}'.format(number, 6, number*6))
print('{} x {:2} = {:2}'.format(number, 7, number*7))
print('{} x {:2} = {:2}'.format(number, 8, number*8))
print('{} x {:2} = {:2}'.format(number, 9, number*9))
print('{} x {:2} = {:2}'.format(number, 10, number*10))
print('-' * 12)
