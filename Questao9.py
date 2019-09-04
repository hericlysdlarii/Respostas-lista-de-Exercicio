#  Faça um Programa que leia três números e mostre-os em ordem decrescente 
#  e em seguida em ordem crescente.  

a = input("digite um numero: ")
b = input("digite um numero: ")
c = input("digite um numero: ")
lista = [a, b, c]
print("Decrescente: " + str(sorted(lista, key=int, reverse=True)))
print("Crescente: " + str(sorted(lista, key=int)))



