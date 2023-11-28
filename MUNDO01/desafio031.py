d = int(input('Digite a distancia da viagem em kms: '))
if d<=200:
    c1 = d*0.5
    print('O valor da passagem será de R$ {} '.format(c1))
else: 
    c2 = d*0.45
    print('O valor da passagem será de R$ {} '.format(c2))
 