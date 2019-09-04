# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira: 
        
#                            Até 5 Kg:              Acima de 5 Kg: 
#            File Duplo      R$ 4,90 por Kg         R$ 5,80 por Kg 
#            Alcatra         R$ 5,90 por Kg         R$ 6,80 por Kg 
#            Picanha         R$ 6,90 por Kg         R$ 7,80 por Kg

# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos
# de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
# Se a compra for feita no cartão Tabajara o cliente receberá ainda um desconto 
# de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade 
# de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações 
# da compra: tipo e quantidade de carne, preço total, tipo de pagamento, 
# valor do desconto e valor a pagar.

def tipoCarne(carne):
 if(carne == 1):
   carne = str("File Duplo")
   return carne
 if(carne == 2):
   carne = str("Alcatra")
   return carne 
 if(carne == 3):
   carne = str("Picanha")
   return carne
def preco(carne, kg):
 if(carne == "File Duplo"):
   if(kg < 5):
     return kg * 4.90
   else:
     return kg * 5.80
 if(carne == "Alcatra"):
   if(kg < 5):
     return kg * 5.90
   else:
     return kg * 6.80
 if(carne == "Picanha"):
   if(kg < 5):
     return kg * 6.90
   else:
     return kg * 7.80
print("Tipos de carne\n")
print("1 - File Duplo\n")
print("2 - Alcatra\n")
print("3 - Picanha\n")
carne = int(input("Qual tipo de carne deseja comprar?"))
carne = tipoCarne(carne)
kg = int(input("\nQuantos kg de " + carne + "?"))
preco = preco(carne, kg)
pagamento = int(input("\nQual tipo de pagamento?\n\t1 - Cartão de credito\n\t2 - Dinheiro\n"))
desconto = 0
if(pagamento == 1):
 desconto = preco * 0.05
 valor = preco - desconto
 pagamento = str("Cartão de credito")
else:
 pagamento = str("Dinheiro")
 valor = preco
 
print("\n\n\nCUPOM FISCAL")
print("\nTipo de carne comprada: ", carne)
print("\nQuantidade de carne comprada (KG): ", kg)
print("\nPreço total (R$): ", preco)
print("\nTipo de pagamento: ", pagamento)
print("\nValor do desconto (R$): ", desconto)
print("\nValor a pagar (R$): ", valor)



