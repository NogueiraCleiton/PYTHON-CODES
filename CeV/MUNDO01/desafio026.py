nome = str(input('Digite uma frase: ')).upper().strip()
#nome.strip()  # .STRIP() REMOVE OS ESPAÇOS NO INICIO E FINAL DA FRASE 
#nome.lower()  # .UPPER() PASSA TODAS AS LETRAS PARA MAIUSCULA 
print('A letra A apareceu {} vezes. '.format(nome.count('A'))) # . count() CONTA A QUANTIDADE DE VEZES QUE ('A') APARECEU
print('A letra A apareceu a primeira vez na posicção {}'.format(nome.find('A')+1)) # .FIND('A') PROCURA A PRIMEIRA VEZ QUE ('A') APARECEU/ PODE SER USADO 
print('A letra A apareceu pela ultima vez na posicão {}'.format(nome.rfind('A')+1)) #rfind.('A') INVERTE O LADO DA CONTAGEM MOSNTRANDO A ULTIMA VEZ QUE APARECEU 
                                                                              # +1 INCLUIDO PARA CONTAGEM SER DE FORMA COMPREENSIVEL HUMANAMENTE           