def soma(n1=0,n2=0):
    n1 = int(input('Digite o n1: '))
    n2 = int(input('Digite o n2: '))
    print(f'A soma de {n1}+{n2} é igual a {n1+n2}')
def subtração(n1=0,n2=0):
    n1 = int(input('Digite o n1: '))
    n2 = int(input('Digite o n2: '))
    print(f'A subtração de {n1}-{n2} é igual a {n1-n2}')
def multiplicação(n1=0,n2=0):
    n1 = int(input('Digite o n1: '))
    n2 = int(input('Digite o n2: '))
    print(f'A multiplação de {n1}*{n2} é igual a {n1*n2}')
def divisão(n1=0,n2=0):
    n1 = int(input('Digite o n1: '))
    n2 = int(input('Digite o n2: '))
    print(f'A divisão de {n1}/{n2} é igual a {n1/n2}')
def exponenciação(n1=0,n2=0):
    n1 = int(input('Digite o n1: '))
    n2 = int(input('Digite o n2: '))
    print(f'A exponenciação de {n1}**{n2} é igual a {n1**n2}')
    
print('-='*20)
print(' '*12,'Calculadora')
print('-='*20)
print('Escolha a função a ser realizada:')
print('SOMA ---> 1')
print('DIVISÃO ---> 2')
print('MULTIPLICAÇÃO ---> 3')
print('EXPONENCIAÇÃO ---> 4')
start = 1
while start == 1:
    f = int(input('Qual Operação deseja realizar:'))
    if f > 0 and f < 4:
            if f == 1:
                soma()
                break
            start = 0
            if f == 2:
                divisão()
                break
            if f == 3:
                multiplicação()
                break
            if f == 4:
                exponenciação()
                break
print('DESEJA CONTINUAR ?')
conf = int(input('1-SIM 2-NÃO'))
if conf in '1,2':
    if conf == 1:
        start = 1
    if conf == 2:
        start = 0
else:
    print('ERR0 OPÇÃO INVALIDA')
    print('Digite apenas 1 ou 2')
    conf = int(input('1-SIM 2-NÃO'))