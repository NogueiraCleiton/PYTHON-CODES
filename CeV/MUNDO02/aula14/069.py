opção = 1
c = maior = homem = m20 = 0
while opção == 1:
    sexo = str(input('Digite seu sexo [M/F]: ')).strip()
    idade = int(input('Digite sua idade: '))
    opção = int(input('Deseja continuar 1-SIM 2-NÃO'))
    c += 1
    if idade >= 18:
        maior += 1
    if sexo in 'Mm':
        homem +=1
    if sexo in "Ff" and idade < 20:
        m20 += 1
print(f'Foi informado {c} pessoas')
print(f'Temos um total de {homem} homens')
print(f'TEmos um total de {m20} mulheres com menos de 20 anos ')
print(f'Temos um total de {maior} pessoas com mais de 18 anos')
print('FIM')
    

