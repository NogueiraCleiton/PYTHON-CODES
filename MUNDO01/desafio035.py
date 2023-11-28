print('-=-=-'*20)
print('Analisador de Triângulos')
print('-=-=-'*20)
n1 = float(input(print('Digite o primeiro segmento: ')))
n2 = float(input(print('Digite o segundo segmento: ')))
n3 = float(input(print('Digite o terceiro segmento: ')))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos formam um triângulo')
else:
    print('Os segmentos não formam um trinângulo') 
