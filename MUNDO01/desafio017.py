from math import hypot
a = int(input('Digite o valor do cateto oposto: '))
b = int(input('Digite o valor do cateto adjacente: '))
h = hypot(a,b)
print ('O valor da hipotenisa é {:.2f}'.format(h)) 