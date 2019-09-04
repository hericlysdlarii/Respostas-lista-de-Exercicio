#  Faça um Programa que peça os 3 lados de um triângulo. 
#  O programa deverá informar se os valores podem ser um triângulo. 
#  Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, 
#  isósceles ou escaleno. 

#   Dicas:
#       Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro; 
#       Triângulo Equilátero: três lados iguais; 
#       Triângulo  Isósceles: quaisquer dois lados iguais; 
#       Triângulo   Escaleno: três lados diferentes. 
 
 
def triangulo(a, b, c):
 
   if not (((a+b)>c) and ((a+c)>b) and ((b+c)>a)):
       print("\nOs aldos informados não formam um triângulo!")
  
   elif (a==b) and (a==c):
       print ("\nO triângulo é equilátero!")
  
   elif a!=b and a!=c and b!=c:
       print ("\nO triângulo é escaleno")
  
   else:
       print ("\nO triângulo é isósceles")
 
a = int(input("Digite o primeira lado: "))
b = int(input("Digite o segunda lado: "))
c = int(input("Digite o terceira Lado: "))

triangulo(a, b, c)







