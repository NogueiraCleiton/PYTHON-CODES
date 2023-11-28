ano = int(input('Digite um ano qualquer: '))
if ano%4 == 0:
    print('O ano digitado foi {} e ele é bisexto'.format(ano))
else:
    print('O ano digitado foi {} e ele não é bisexto'.format(ano))