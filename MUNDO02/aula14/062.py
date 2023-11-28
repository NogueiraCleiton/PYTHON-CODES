print('='*40)
print(' '*5,'10 TERMOS DE UMA PA',' '*5)
print('='*40)
primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão:'))
pa = primeiro + razão
termo = 10 
while termo != 0:
    print('{}'.format(pa), end=' > ')
    termo -= 1
    pa += razão
    if termo == 0:
        termo = int(input('Quer mostrar mais quantos termos: ')) 
        if termo == 0:
            print('')
        else:
            print('{}'.format(pa), end=' > ')
            termo -= 1
            pa += razão
print('Acabou')