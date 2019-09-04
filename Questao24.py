#  Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: 
#        "Telefonou para a vítima?" 
#        "Esteve no local do crime?" 
#       "Mora perto da vítima?" 
#        "Devia para a vítima?"
#        "Já trabalhou com a vítima?" 

#  O programa deve no final emitir uma classificação sobre a participação da pessoa 
#  no crime. Se a pessoa responder positivamente a 2 questões ela deve ser 
#  classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
#  Caso contrário, ele será classificado como "Inocente". 


res1 = input("Telefonou para a vítima? ")
res2 = input("Esteve no local do crime? ")
res3 = input("Mora perto da vítima? ")
res4 = input("Devia para a vítima? ")
res5 = input("Já trabalhou com a vítima? ")
 
lista = [res1, res2, res3, res4, res5]
 
if ((lista.count('sim')) == 2):
   print("\nSuspeita")
elif ((lista.count('sim')) >= 3 and (lista.count('sim')) <= 4):
   print("\nCúmplice")
elif ((lista.count('sim')) == 5):
   print("\nAssassino")
else:
   print("\nInocente")








