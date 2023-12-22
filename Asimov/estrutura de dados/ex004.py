def nota(n1=0,n2=0):
    media = (n1+n2)/2
    print(f'Sua média foi {media}')
    if media >= 7 and media <=9:
        print('APROVADO')
    if media < 7:
        print('REPOROVADO')
    if media == 10:
        print('APROVADO COM DISTINÇÃO')


print('=-'*20)
print('RESULTADO FINAL')
print('=-'*20)
n1 = float(input('Digite a sua 1ª nota:'))
n2 = float(input('Digite a sua 2ª nota: '))
nota(n1,n2)