#  Faça um programa que pergunte o preço de três produtos e informe qual
#  produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. 

a = float(input("digite o preço do produto 1: "))
b = float(input("digite o preço do produto 2: "))
c = float(input("digite o preço do produto 3: "))
lista = [a, b, c]
print("Voce deve comprar que custa " + str(min(lista)))



