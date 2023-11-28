n = int(input('Quer ver a tabuada de qual valor ?'))
print('-=-'*20)
while n > 0:
    for c  in range (1,11):
        print(f'{n} x {c}  =  {n*c}')
        c += 1
    print('-=-'*20)
    n = int(input('Quer ver a tabuada de qual valor ?'))
    print('-=-'*20)
print('FINAL DO PROGRAMA')
