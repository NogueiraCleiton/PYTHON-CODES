#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
#mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores***
print('='*40)
print(' '*5,'GRUPO DE MAIOR IDADE',' '*5)
print('='*40)
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nascimento = int(input('Digite seu ano de nascimento: '))
    idade = atual - nascimento
    if idade >= 21:
       totmaior += 1
    else:
       totmenor += 1
print('Ao todo tivemos {} pessoas de maior'.format(totmaior))
print('Também tivemos {} pessoa menor'.format(totmenor))

