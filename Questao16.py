#  Faça um programa que calcule as raízes de uma equação do segundo grau, 
#  na forma ax 2 + bx + c = 0. O programa deverá pedir os valores de a, b 
#  e c e fazer as consistências, informando ao usuário nas seguintes situações: 

#    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau 
#    e o programa não deve solicitar os demais valores, sendo encerrado com a mensagem 
#    “Equação de 2o. Grau inválida. O valor da variável a deve ser maior que zero; 

#    Se o delta calculado for negativo, a equação não possui raízes reais.
#    Informe ao usuário e encerre o programa; 

#    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; 
#    informe ao usuário; 

#    Se o delta for positivo, a equação possui duas raízes reais; informe-as ao usuário;
 
 
def equaçao2grau(a, b, c):
   delta = (b**2) - (4*a*c)
   print("\nDelta: " +str(delta))
   if (delta < 0):
       raise SystemExit("\nA equação não possui raízes reais!")
   if (delta == 0):
       print("\nA equação possiui apenas uma raiz real!")
   if (delta > 0):
       print("\nA equação possiui duas raízes reais!")
 
   x1 = (-b + (delta ** (1/2))) / (2*a)
   x2 = (-b - (delta ** (1/2))) / (2*a)
   print("\nx1: " + str(x1))
   print("x2: " + str(x2))     
 
a = float(input("a: "))
if (a == 0):
   raise SystemExit("Equação do 2º grau inválida")
b = float(input("b: "))
c = float(input("c: "))
 
equaçao2grau(a, b, c)








