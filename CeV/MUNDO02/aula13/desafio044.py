pagamento = int(input('digite a forma de pagamento: 1-a vista 2-cartão: '))
if pagamento == 1:
  avista = int(input("Escolha a forma de parcelamento 1-DINHEIRO 2-CHEQUE "))
  print('Seu desconto será de 10%') 
elif pagamento == 2:
   cartao = int(input('Escolha a forma de parcelamento 1-à vista 2-em 2x vezes 3-em 3x vezes ou mais'))
   if cartao == 1:
       print('seu desconto será de 5%')
   elif cartao == 2:
       print('vc pagar preco normal ')
   elif cartao == 3:
       print('seu produto tera acresimo de 20% ') 