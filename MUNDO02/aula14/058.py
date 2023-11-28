'''Melhore o jogo do DESAFIO 028 aonde o computador vai pensar em um numeor enre 0-10
 Só que agora o jogador vai tentar advinhar até acertar, mostrando quantas palpites foram necessarios para vencer'''
from random import randint
from time import sleep
palpites = 1
num = randint(0,10)
print('-=-'*20)
print('Vou pensar me um numero entre 0-10')
print('-=-'*20)
sleep(1)
jogador = int(input('Em que numero eu pensei ? '))
print('PROCESSANDO...')
sleep(1)
while jogador != num:
        if jogador > num:
            print('Menos... tente novamente')
        else:
            print('Mais... Tente novamente') 
        palpites += 1 
        jogador = int(input(' Você errou digite novamente um numero entre 0-10:')) 
jogador == num
print('PARABENS VOCÊ ACERTOU foi necessario {} palpites'.format(palpites))