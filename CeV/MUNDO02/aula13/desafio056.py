#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
#a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaidade = 0
mediaidade = 0
totmulher = 0
nomevelho = ''
maioridadehomem = 0 
for c in range (1,5):
    print('-----{}ª PESSOA-----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('sexo [M/F]')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade 
        nomevelho = nome 
    if sexo in 'Mm' and idade > maioridadehomem:
        nomevelho = nome 
        maioridadehomem = idade
    if sexo in 'Ff' and idade < 20:
        totmulher += 1 
mediaidade = somaidade/4
print ('A média de idade é {} anos '.format(mediaidade))
print('O homem mais velho é {} com {} anos'.format(nomevelho, maioridadehomem))
print('Ao todo temos {} mulheres com menos de 20 anos'.format(totmulher))      