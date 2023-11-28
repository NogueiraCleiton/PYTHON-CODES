n1 = int(input('Digite três numeros: '))
n2 = int(input('Digite três numeros: '))
n3 = int(input('Digite três numeros: '))
lista = [n1,n2,n3]
n2 = sorted(lista)
print('O maior numero informado foi {}'.format(n2[2]))
print('O menor numero informado foi {}'.format(n2[0]))
