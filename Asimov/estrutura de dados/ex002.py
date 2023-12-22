'''
Crie um program que leia atraves do metodo input, 
o nome completo de uma pessoa e cumprimente-a apenas pelo primeiro nome 
'''

nome = str(input('Qual seu nome ')).split()
print(f'prazer {nome[0]}')
