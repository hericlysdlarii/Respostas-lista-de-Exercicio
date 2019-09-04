#  Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
#      
#        Álcool: 
#            Até 20 litros, desconto de 3% por litro 
#            Acima de 20 litros, desconto de 5% por litro 
#        Gasolina: 
#            Até 20 litros, desconto de 4% por litro 
#            Acima de 20 litros, desconto de 6% por litro 

#  Escreva um programa que leia o número de litros vendidos, o 
#  tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
#  calcule e imprima o valor a ser pago pelo cliente sabendo-se que
#  o preço do litro da gasolina é R$ 3,45 o preço do litro do álcool é R$ 4,39. 


litros_vendidos = float(input("Digite a quantidade de litros vendidos: "))
tipo_combustivel = input("Tipo de combustível: ")
 
if (litros_vendidos <= 20 and tipo_combustivel == 'A'):
   valor = litros_vendidos * 4.39
   valor_pago = valor - (valor*0.03)
   print('Valor a ser pago: ', valor_pago)
elif (litros_vendidos > 20 and tipo_combustivel == 'A'):
   valor = litros_vendidos * 4.39
   valor_pago = valor - (valor*0.05)
   print('Valor a ser pago: ', valor_pago)
elif (litros_vendidos <= 20 and tipo_combustivel == 'G'):
   valor = litros_vendidos * 3.45
   valor_pago = valor - (valor*0.04)
   print('Valor a ser pago: ', valor_pago)
elif (litros_vendidos > 20 and tipo_combustivel == 'G'):
   valor = litros_vendidos * 3.45
   valor_pago = valor - (valor*0.06)
   print('Valor a ser pago: ', valor_pago)








