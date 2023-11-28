from random import randint
from time import sleep # função para aguardar periodo 
computador = randint(0,5) # faz o computador escolher um numero entre 0 e 5
print('-=-'*20)
print('Vou pensar me um numero...')
print('-=-'*20)
jogador = int(input('Em que numero eu pensei ? '))
print('PROCESSANDO...')
sleep(3)
if computador == jogador:
    print ('Você acertou o numero sorteado foi {}'. format(computador))
else:
    print('Você errou o numero sorteado foi {}'. format(computador))

