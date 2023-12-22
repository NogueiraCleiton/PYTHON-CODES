vel = float(input('Digite a velocidade do carro: '))
if vel >= 81:
    m = (vel-80)*7
    print('Você ultrapassou o limite de velocidade e foi multado em {}'.format(m))
else:
    print('Dirija sempre com segurança e utilize cinto !')