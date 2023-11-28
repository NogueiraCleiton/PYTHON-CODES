'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
CAso esteja errado, peça a digitação novamente até ter um valor correto'''

sexo = str(input('Digite seu sexo [M/F]:')).upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    print('ERRO valor digitado invalido')
    sexo = str(input('Digite novamente seu sexo [M/F]:')).upper().strip()[0]
print('O sexo digitado foi {}'.format(sexo))