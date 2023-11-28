n1 =  cont = total = 0 
while True:
    n1 = int(input('Digite um numero (999 para parar): '))
    if n1 == 999:
        break
    total += n1
    cont += 1
print(f'Você digitou {cont} e a soma dos valores foi {total}')