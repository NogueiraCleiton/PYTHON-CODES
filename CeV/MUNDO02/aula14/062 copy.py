print('='*40)
print(' '*5,'10 TERMOS DE UMA PA',' '*5)
print('='*40)
primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão:'))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' > ')
    termo += razão
    cont +=1 
print('Acabou')