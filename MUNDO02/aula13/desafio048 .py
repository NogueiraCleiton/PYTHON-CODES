# print soma de numeros impares entre 1-500 
s = 0
cont = 0
for c in range (0,500,3):
    if c%2 > 0:
        cont = cont +1
        s += c
print ('O valor da soma dos {} numeros impares entre 1 e 500 é {}'.format(cont,s),end='.')