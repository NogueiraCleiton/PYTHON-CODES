num = int(input('Digite um numero interio: '))
print('''escolha uma das bases para conversão:
      [1] Converter para BINAÁRIO
      [2] Converter para OCTAL 
      [3] Converter para HEXADECIMAL''')
opção = int(input('Digite sua opção:'))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif opção == 3: 
    print('{} convertifo para HEXADECIMAL é igual a{}'.format(num,hex(num)[2:]))
else:
    print('Opção invalida. Tente novamente. ')