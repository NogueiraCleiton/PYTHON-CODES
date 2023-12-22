#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
print('='*40)
print(' '*5,'VERIFICADOR DE NUMERO PRIMO',' '*5)
print('='*40)
num = int(input('Digite um numero: '))
tot = 0
for c in range (1,num+1,):
    if num % c == 0 :
        print('\033[34m',end=' ')
        tot += 1
    else:
        print('\033[m',end=' ')
    print('{}'.format(c),end=' ')
print('\n\033[mO número {} foi divísivel {} vezes'.format(num,tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('e por iso ele NÃO É PRIMO!')