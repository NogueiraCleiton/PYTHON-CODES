# digite um numero e mostre sua fatorial 
from time import sleep
n1 = int(input('Digite um valor para calcular seu fatorial: '))
c = n1
f = 1
print(f'Calculando o fatorial de {n1}!')
sleep(1)
while c > 0:
    print(f'{c}',end='')
    print(' x '  if c > 1 else ' = ' , end='')
    f *= c
    c -= 1
print(f)
print(f'O fatorial de {n1} é igual a {f}')
    
    
    
    