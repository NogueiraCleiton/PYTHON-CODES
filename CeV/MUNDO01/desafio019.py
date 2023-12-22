# funcao chice para sorteio aleatorio de 1 valor 

import random
a = str(input('Digite seu nome: '))
b = str(input('Digite seu nome: '))
c = str(input('Digite seu nome: '))
d = str(input('Digite seu nome: '))
lista =[a,b,c,d]
escolhido = random.choice(lista)
print('O aluno esclhido foi {}'.format(escolhido))
