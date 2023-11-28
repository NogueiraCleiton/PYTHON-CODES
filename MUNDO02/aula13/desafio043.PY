from time import sleep
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura*altura)
print('-=-'*20)
print('CALCULANDO SEU IMC, AGUARDE...')
print('-=-'*20)
sleep(1)
if imc <18.5:
    print('Seu IMC é de {:.2f}, você está Abaixo do peso!'.format(imc))
elif imc == 18.5 and imc <=25:
    print('Seu IMC é de {:.2f}, você está com peso ideal!'.format(imc))
elif imc >25 and imc <= 30:
    print('Seu IMC é de {:.2f}, você está com sobrepeso!'.format(imc))
elif imc >30 and imc <=40:
    print('Seu IMC é de {:.2f}, você está com obesidade!'.format(imc))
else:
    print('Seu IMC é de {:.2f}, você está com obesidade morbida!'.format(imc))