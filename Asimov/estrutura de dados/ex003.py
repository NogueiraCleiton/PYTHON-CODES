'''
Crie um program queextaria o dominio de um email informado
'''

email = str(input('Qual seu e-mail ')).strip()
dominio = email.split('@')[-1]
print(f'O dominio infomrado foi {dominio}') 
    
        
