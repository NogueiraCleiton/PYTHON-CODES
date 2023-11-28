from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
cat =  ano-nascimento
from time import sleep
print('-=-'*20)
print('CALCULANDO SUA CATEGORIA...')
print('-=-'*20)
sleep(3)
if cat <9 or cat == 9:
    print('Você tem {} anos, sua categortia é MIRIM.'.format(cat))
elif cat < 10 or cat == 14:
    print('Você tem {} anos, sua categortia é INFANTIL.'.format(cat))
elif cat < 19 or cat == 19:
    print('Você tem {} anos, sua categortia é JUNIOR.'.format(cat))
elif cat < 20 or cat == 20:
    print('Você tem {} anos, sua categortia é SENIOR.'.format(cat))
else:
    print('Você tem {} anos, sua categortia é MASTER.'.format(cat))
    