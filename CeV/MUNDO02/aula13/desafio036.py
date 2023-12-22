valordacasa = float(input('Digite o valor da casa R$: '))
salario = float(input('Digite o valor do seu salario R$: '))
prazopagamento = float(input('Digite o prazo para pagamento em meses: '))
prestacao = valordacasa/prazopagamento
limite = salario*30/100
if prestacao>limite:
    print('\033[7;31;44mEmprestimo negado\033[0;0;0m, o valor ultrapassa 30% do seu salário')
else:
    print('\033[7;32;40mEmprestimo aprovado\033[0;0;m, no valor de R${:.3f} sendo em {:.0f}X de R${:.3f}'.format(valordacasa,prazopagamento,prestacao))