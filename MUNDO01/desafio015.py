km = float(input('Digite o nº de quilometros rodados: '))
dias = int(input('Digite a quantidade de dias: '))
tkm = km * 0.15
tdias = dias * 60
total = tkm+tdias
print('O total a ser pago é R${:.2f} \n Sendo R${:.2f} pelos Kms rodas e R${:.2f} pelos dias'.format(total,tkm,tdias))