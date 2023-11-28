'''Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, 
que é a condição de parada. No final, 
mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
n1 = int(input('Digite numero: '))
soma = n1
total = 0
while n1 != 999:
    n1 = int(input('Digite numero: ')) 
    soma += n1
    total +=1 
    if n1 == 999:
        soma -= 999
        print('Fim do programa Foram digitados {} valores e a soma dos valores informados é {}'.format(total,soma))