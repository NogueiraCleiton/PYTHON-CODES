from datetime import date
nascimento = int(input('Digite o ano de seu nascimento: '))
ano = date.today().year
idade = ano - nascimento
tempo = int(18-idade)
if tempo < 0:
    tempo = tempo*-1
if idade > 18:
    print('Já passou {} anos do periodo de se alistar no serviço militar!'.format(tempo))
elif idade < 18:
    print('Você ainda vai se alistar no serviço militar! Faltam {} anos'.format(tempo))
elif idade == 18:
    print('Está na hora de se alistar no serviço militar!')
print (tempo)