# Faça um programa para o cálculo de uma folha de pagamento, 
# sabendo que os descontos são: Imposto de Renda, que depende 
# do salário bruto (conforme tabela abaixo), 10% INSS, 3% Sindicato 
# de classe e FGTS correspondendo a 11% do Salário Bruto. 
# Detalhe o FGTS não é descontado do salário do funcionário (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá solicitar ao usuário o valor da sua hora e a quantidade de horas 
# trabalhadas no mês. 

#    Tabela de desconto do IR: 
#        Salário Bruto até R$ 900,00 - isento 
#        Salário Bruto até R$ 1.500,00 - desconto de 5% 
#        Salário Bruto até R$ 2.500,00 - desconto de 10% 
#        Salário Bruto acima de R$ 2.500,00 - desconto de 20% 

#    Imprimir na tela as informações, dispostas conforme o exemplo abaixo. 
#    No exemplo o valor da hora é R$ 5,00 e a quantidade de horas trabalhadas 
#    no mês é 220 horas. 

#       Salário Bruto: (5 * 220): R$ 1.100,00 
#        (-) IR (5%)...............: R$ 55,00 
#       (-) INSS (10%)...........: R$ 110,00 
#        (-) Sindicato (3%)........: R$ 33,00 
#        FGTS (11%)..............: R$ 121,00 
#        Total de descontos.......: R$ 198,00 
#        Salário Líquido...........: R$ 902,00 



def folha(valor, horas):
 
   salario_bruto = valor * horas
 
   if (salario_bruto <= 900):
       print("Salario Bruto: " + str(salario_bruto))
       print("(-) IR: Isento")
       print("(-) INSS: " + str(salario_bruto*0.1))
       print("(-) Sindicato: " + str(salario_bruto*0.03))
       print("FGTS: " + str(salario_bruto*0.11))
       print("Total de desc: " + str((salario_bruto*0.1) + (salario_bruto*0.03)))
       print("Salario liquido: " + str(salario_bruto - ((salario_bruto*0.1) + (salario_bruto*0.03))))
 
   if ((salario_bruto > 900) and (salario_bruto <= 1500)):
       print("Salario Bruto: " + str(salario_bruto))
       print("(-) IR: " + str(salario_bruto*0.05))
       print("(-) INSS: " + str(salario_bruto*0.1))
       print("(-) Sindicato: " + str(salario_bruto*0.03))
       print("FGTS: " + str(salario_bruto*0.11))
       print("Total de desc: " + str((salario_bruto*0.1) + (salario_bruto*0.03) + (salario_bruto*0.05)))
       print("Salario liquido: " + str(salario_bruto - ((salario_bruto*0.1) + \
       (salario_bruto*0.03 + (salario_bruto*0.05)))))
  
   if ((salario_bruto > 1500) and (salario_bruto <= 2500)):
       print("Salario Bruto: " + str(salario_bruto))
       print("(-) IR: " + str(salario_bruto*0.1))
       print("(-) INSS: " + str(salario_bruto*0.1))
       print("(-) Sindicato: " + str(salario_bruto*0.03))
       print("FGTS: " + str(salario_bruto*0.11))
       print("Total de desc: " + str((salario_bruto*0.1) + (salario_bruto*0.03) + (salario_bruto*0.1)))
       print("Salario liquido: " + str(salario_bruto - ((salario_bruto*0.1) + \
       (salario_bruto*0.03+ (salario_bruto*0.1)))))
   
   if (salario_bruto > 2500):
       print("Salario Bruto: " + str(salario_bruto))
       print("(-) IR: " + str(salario_bruto*0.2))
       print("(-) INSS: " + str(salario_bruto*0.1))
       print("(-) Sindicato: " + str(salario_bruto*0.03))
       print("FGTS: " + str(salario_bruto*0.11))
       print("Total de desc: " + str((salario_bruto*0.1) + (salario_bruto*0.03) + (salario_bruto*0.2)))
       print("Salario liquido: " + str(salario_bruto - ((salario_bruto*0.1) + \
       (salario_bruto*0.03+ (salario_bruto*0.2)))))
 
valor = float(input("Valor da hora: "))
horas = float(input("Horas trabalhadas: "))
folha(valor, horas)





