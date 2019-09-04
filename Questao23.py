#  Faça um Programa que leia 2 números e em seguida pergunte 
#  ao usuário qual operação ele deseja realizar. O resultado da 
#  operação deve ser acompanhado de uma frase que diga se o número é: 

#    Par ou ímpar; 
#    Positivo ou negativo; 
#    Inteiro ou decimal.


x = float(input('Digite um número: '))
y = float(input('Digite um número: '))
 
escolha = int(input('''
   Qual operação matemática deseja fazer?
      
   1 - Soma
   2 - Subtração
   3 - Multiplicação
   4 - Divisão
      
   Escolha: '''))
 
if (escolha == 1):
   print('\nResultado: ', x+y)
   if ((x+y) % 2 == 0):
       print("Número Par")
   else:
       print("Número Ímpar")
   if ((x+y) >= 0):
       print("Positivo")
   else:
       print("Negativo")
   if ((x+y) == round(x+y)):
       print("Inteiro")
   else:
       print("Decimal")
 
if (escolha == 2):
   print('\nResultado: ', x-y)
   if ((x-y) % 2 == 0):
       print("Número Par")
   else:
       print("Número Ímpar")
   if ((x-y) >= 0):
       print("Positivo")
   else:
       print("Negativo")
   if ((x-y) == round(x-y)):
       print("Inteiro")
   else:
       print("Decimal")
 
if (escolha == 3):
   print('\nResultado: ', x*y)
   if ((x*y) % 2 == 0):
       print("Número Par")
   else:
       print("Número Ímpar")
   if ((x*y) >= 0):
       print("Positivo")
   else:
       print("Negativo")
   if ((x*y) == round(x*y)):
       print("Inteiro")
   else:
       print("Decimal")
 
if (escolha == 4):
   print('\nResultado: ', x/y)
   if ((x/y) % 2 == 0):
       print("Número Par")
   else:
       print("Número Ímpar")
   if ((x/y) >= 0):
       print("Positivo")
   else:
       print("Negativo")
   if ((x/y) == round(x/y)):
       print("Inteiro")
   else:
       print("Decimal")








