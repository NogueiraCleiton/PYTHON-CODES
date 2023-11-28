#Detector de Palíndromo
print('='*40)
print(' '*5,'DETECTOR DE PALINDROMO',' '*5)
print('='*40)
frase = str(input('Digite uma frase ou palavra: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print('O inveros de {} é {} '.format(frase,inverso))
if junto == inverso:
    print('Temos um palíndromo')
else:
    print('A frase não é um palíndromo')
    