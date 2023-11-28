# funcao shuffle para sorteio de ordem de apresnetação 

import random
a = str(input('Digite seu nome: '))
b = str(input('Digite seu nome: '))
c = str(input('Digite seu nome: '))
d = str(input('Digite seu nome: '))
lista =[a,b,c,d]
random.shuffle(lista)
print(lista)