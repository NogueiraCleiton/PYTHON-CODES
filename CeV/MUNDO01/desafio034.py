salario = float(input('Digite seu salario R$  '))
if salario <= 1250 :
    aumento2 = (salario/100)*15
    salnovo2 = salario+aumento2
    print('Seu novo salario é de r$ {}'.format(salnovo2))
else: 
    aumento1 = (salario/100)*10
    salnovo1 = salario+aumento1
    print('Seu novo salario é de R$ {}'.format(salnovo1))
