print('='*40)
print(' '*5,'10 TERMOS DE UMA PA',' '*5)
print('='*40)
primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=' > ')
        termo += razão
        cont +=1 
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar ?'))
print('FIM')