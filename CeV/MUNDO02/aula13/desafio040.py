from time import sleep                                       
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print('-=-'*20)
print('CALCULANDO SUA NOTA...')
print('-=-'*20)
sleep(3)
print('Sua nota média foi {}!'.format(media))
if media < 5:
    print('Média abaixo de 5.00: \033[0;31;40m REPROVADO \033[m')
if media > 5 and media < 6.9:
    print('Média entre 5.00 e 6.9; \033[0;31;40m RECUPERAÇÃO \033[m')
if media > 7:
    print('Média maior que 7.0 \033[0;32;40m APROVADO \033[m')    
