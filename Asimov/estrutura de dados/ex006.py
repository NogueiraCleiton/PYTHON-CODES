from time import sleep
nome = str(input('Digite seu nome: '))
for p in range(len(nome)+1):
    print(nome[:p])
    sleep(0.5)

 
    