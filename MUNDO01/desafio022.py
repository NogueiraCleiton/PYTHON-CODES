nome = input('Digite seu nome completo: ')
print('Analisando seu nome...')
print('Seu nome em maiusculas é:' +nome.upper())
print('Seu nome em minusculas é: '+nome.lower())
print('Seu nome completo tem: {} caracteres'.format(len(nome) - nome.count(' ')))
nome1 = nome.split()
c = nome1[0]
print('Seu primeiro nome tem:{} letras'.format(nome.find(' ')))

print('Seu primeiro nome é {} e tem {} letras'.format(c,len(c[0:])))