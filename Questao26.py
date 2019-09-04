# Uma fruteira está vendendo frutas com a seguinte tabela de preços: 

#            Até 5 Kg:                        Acima de 5 Kg:
#            Morango R$ 2,50 por Kg           R$ 2,20 por Kg
#            Maçã R$ 1,80 por Kg              R$ 1,50 por Kg 

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra 
# ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
# Escreva um programa para ler a quantidade (em Kg) de morangos e a quantidade 
# (em Kg) de maçãs adquiridas e escreva o valor a ser pago pelo cliente. 

morangos_kg = float(input("Digite quantos kg de morango: "))
maças_kg = float(input("Digite quantos kg de maçã:: "))
 
if (morangos_kg <= 5.0):
   preço_morango = morangos_kg * 2.50
   if (maças_kg <= 5.0):
       preço_maça = maças_kg * 1.80
       if ((morangos_kg + maças_kg) > 8.0 or (preço_morango + preço_maça) > 25.0):
           total = preço_morango + preço_maça
           total_pagar = total - (total*0.1)
           print("\nTotal a ser pago:", total_pagar)
       else:
           print("\nTotal a ser pago: ", preço_morango + preço_maça)
   else:
       if (maças_kg > 5.0):
           preço_maça = maças_kg * 1.50
           if ((morangos_kg + maças_kg) > 8.0 or (preço_morango + preço_maça) > 25.0):
               total = preço_morango + preço_maça
               total_pagar = total - (total*0.1)
               print("\nTotal a ser pago:", total_pagar)
           else:
               print("\nTotal a ser pago: ", preço_morango + preço_maça)
 
if (morangos_kg > 5.0):
   preço_morango = morangos_kg * 2.20
   if (maças_kg <= 5.0):
       preço_maça = maças_kg * 1.80
       if ((morangos_kg + maças_kg) > 8.0 or (preço_morango + preço_maça) > 25.0):
           total = preço_morango + preço_maça
           total_pagar = total - (total*0.1)
           print("\nTotal a ser pago:", total_pagar)
       else:
           print("\nTotal a ser pago: ", preço_morango + preço_maça)
   else:
       if (maças_kg > 5.0):
           preço_maça = maças_kg * 1.50
           if ((morangos_kg + maças_kg) > 8.0 or (preço_morango + preço_maça) > 25.0):
               total = preço_morango + preço_maça
               total_pagar = total - (total*0.1)
               print("\nTotal a ser pago:", total_pagar)
           else:
               print("\nTotal a ser pago: ", preço_morango + preço_maça)








