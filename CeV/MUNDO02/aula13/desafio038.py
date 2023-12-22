from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('-=-'*20)
print('Analisando os valores informados...')
print('-=-'*20)
sleep(3)
if n1 > n2:
    print('O primeiro valor é maior !')
elif n2 > n1:
    print('O segundo valor é maior !')
else:
    print('Não existe valor maior, os dois valores são iguais !')