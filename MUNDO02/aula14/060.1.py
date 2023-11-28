# digite um numero e mostre sua fatorial 
from time import sleep
from math import factorial
n1 = int(input('Digite um valor para calcular seu fatorial: '))
n2 = n1
f = 1
c = n1
print(f'Calculando o fatorial de {n1}!')
sleep(1)
for n1 in range(n1,0,-1):
    print(n1, end='')
    print(' x ' if n1>1 else ' = ',end='')
    f *= c
    c -= 1
print(f)
print(f'O fatorial de {n2} é igual a {f}')
    
    
    

