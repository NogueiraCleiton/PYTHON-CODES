# leia 6 numeros e mostre a soma dos numeros pares 
soma = 0
cont = 0
for c in range (1,7):
    n1 = int(input('Digite {} numero: '.format(c)))
    if n1%2 == 0:
        soma += n1
        cont += 1
print('Você informou {} númers PARES e a soma foi {}'.format(cont,soma))
