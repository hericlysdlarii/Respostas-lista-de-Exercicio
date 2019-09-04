#  Faça um Programa para um caixa eletrônico. 
#  O programa deverá perguntar ao usuário a valor do saque e 
#  depois informar quantas notas de cada valor serão fornecidas. 
#  As notas disponíveis serão as de 2, 5, 10, 50 e 100 reais. 
#  O valor mínimo é de 10 reais e o máximo de 600 reais. 
#  O programa não deve se preocupar com a quantidade de notas existentes na máquina. 

#  Exemplo 1: Para sacar a quantia de 257 reais, o programa fornece duas notas de 100, 
#  uma nota de 50, uma nota de 5 e uma nota de 2; 

#  Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, 
#  uma nota de 50, quatro notas de 10, uma nota de 5 e duas notas de 2. 


numero = int(input('Valor para sacar (OBS: valor entre 10 e 600): '))
if (numero < 10 or numero > 600):
 raise SystemExit("Valor inválido")
cem = int(numero / 100)
numero = numero - (cem*100)
  
cinquenta = int(numero/50)
numero = numero - (cinquenta*50)
 
dez = int(numero/10)
numero = numero - (dez*10)
 
cinco = int(numero/5)
numero = numero - (cinco*5)
 
um = numero
  
print('Notas R$100,00 = ',cem)
print('Notas R$ 50,00 = ',cinquenta)
print('Notas R$ 10,00 = ',dez)
print('Notas R$  5,00 = ',cinco)
print('Notas R$  1,00 = ',um)








