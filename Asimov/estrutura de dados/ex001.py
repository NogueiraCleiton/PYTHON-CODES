'''
Crie um program que leia atraves do metodo input, 
idade, peso e mostre na tela o IMC da pessoa
'''

peso = float(input('Qual seu peso'))
altura = float(input('Qual sua altura: '))
IMC = peso/(altura**2)
print(f'{IMC:.2f}')