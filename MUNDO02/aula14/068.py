from random import randint
v = 0
while True:
    jogador = int(input('Digite um numero: '))
    cpu = randint(0,10)
    total = jogador + cpu
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR OU IMPAR [P/I]')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {cpu}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0: 
            print('Voce Venceu ')
            v += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu')
            v += 1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamnente...')
print(f'GAME OVER! Você venceu {v} vezes.')