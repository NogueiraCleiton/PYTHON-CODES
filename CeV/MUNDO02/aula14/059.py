''' Crie um programa que leia 2 valores e mostre o menu com as opções
[1] soma [2] multilplicar [3] maior [4] novos numeros [5] sair do programa'''
opção = 0
while opção != 4:
    n1 = float(input('Digite o primeiro numero: '))
    n2 = float(input('Digite o segundo numero: '))
    print('-=-'*20)
    print('ESCOLHA UMA DAS OPÇÕES')
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR VALOR')
    print('[4] NOVOS NUMEROS')
    print('[5] SAIR')
    print('-=-'*20)
    opção = int(input('Selecione uma das opções '))
    if opção == 1:
        soma = n1 +n2 
        print('A soma dos valores de {} mais {} é igual a {}'.format(n1,n2,soma))
        break
    if opção == 2:
        mult = n1*n2
        print('O valor de {} multiplicado por {} é igual a {}'.format(n1,n2,mult))
        break
    if opção == 3:
        if n1 > n2:
            print('O maior valor digitado foi {}'.format(n1))
            break
        if n2 > n1:
            print('O mairo valor digitado foi {}'. format(n2))
            break
        if n1 == n2:
            print('Os valores de {} e {} são iguais'.format(n1,n2))
            break
    if opção == 5:
        print('Saiu do programa: ')
        break    
    while opção == 4:
        opção = 0
'''n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
opção = int(input('Selecione uma das opções '))'''