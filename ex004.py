n = input('Digite algo: ')
print('O tipo primitivo é ', type(n))
print('{} só tem espaços? '.format(n), n.isspace())
print('{} é um número?'.format(n), n.isnumeric())
print('{} é alfabético?'.format(n), n.isalpha())
print('{} é alfanumérico'.format(n), n.isalnum())
print('{} está somente em maiúsculas?'.format(n), n.isupper())
print('{} está somente em minúculas?'.format(n), n.islower())
print('{} está capitalizada?'.format(n), n.istitle()) #quando a palavra tem maiúscula e minúscula
