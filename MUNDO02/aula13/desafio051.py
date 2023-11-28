#progressão aritmetica
print('='*40)
print(' '*5,'10 TERMOS DE UMA PA',' '*5)
print('='*40)
primeiro = int(input('Primeiro termo:'))
razão = int(input('Razão:'))
decimo = primeiro + (11-1) * razão
for c in range (primeiro,decimo+razão,razão):
    print('{}'.format(c), end=' > ')
print('Acabou')