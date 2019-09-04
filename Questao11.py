# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores. 
# Desenvolver um programa que atenda as necessidades de cálculo para os reajustes de 
# acordo com os requisitos abaixo: 

#    Receber como entrada o salário do colaborador e em seguida o programa deve atribuir 
#    o percentual de reajuste como segue:

#        Salário até R$ 280,00: aumento de 20%.
#        Salário acima de R$ 280,00 até R$ 700,00: aumento de 15%.
#        Salário acima de R$ 700,00 até R$ 1.500,00: aumento de 10%. 
 #       Salário acima R$ 1500,00: aumento de 5%.
        
#    Após o aumento ser realizado, informar na tela: 

#        O salário antes do reajuste; 
#        O percentual de aumento aplicado; 
#        O valor do aumento; 
#        O valor do salário reajustado (após o aumento). 


def reajuste(salario):
   if (salario <= 280):
      new_salario = salario + (salario*0.2)
      print("Salario: " + str(salario))
      print("% de aumento: 20%")
      print("Valor do aumento: " + str(salario*0.2))
      print("Novo salario: " + str(new_salario))
   if ((salario > 280) and (salario <= 700)):
      new_salario = salario + (salario*0.15)
      print("Salario: " + str(salario))
      print("% de aumento: 15%")
      print("Valor do aumento: " + str(salario*0.15))
      print("Novo salario: " + str(new_salario))
   if ((salario > 700) and (salario <= 1500)):
      new_salario = salario + (salario*0.1)
      print("Salario: " + str(salario))
      print("% de aumento: 10%")
      print("Valor do aumento: " + str(salario*0.1))
      print("Novo salario: " + str(new_salario))
   if (salario > 1500):
      new_salario = salario + (salario*0.05)
      print("Salario: " + str(salario))
      print("% de aumento: 5%")
      print("Valor do aumento: " + str(salario*0.05))
      print("Novo salario: " + str(new_salario))
      
salario = float(input("Digite o salario: "))
reajuste(salario)




