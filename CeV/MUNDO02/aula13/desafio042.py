print('-=-'*20)
print('ANALISADOR DE TRIANGULOS')
print('-=-'*20)
n1 = float(input('Digite o primeiro segmento:'))
n2 = float(input('Digite o segundo segmento:'))
n3 = float(input('Digite o terceiro segmento:'))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos formam um triângulo')
    if n1 == n2 == n3:
        print('Triangulo do tipo Equilatero com todos os lados iguais')
    elif n1 == n2 or n1 == n3 or n3 == n2:
        print('Triangulo do tipo Isoceles com dois lados iguais')
    else:
        print('Triangulo do tipo Escaleno com todos os lados diferentes')
else:
    print('Os segmentos não formam um trinângulo') 
