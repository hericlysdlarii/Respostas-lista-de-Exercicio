#  Faça um Programa que leia um número e exiba o nome do dia correspondente da semana. 
#  (1-Domingo, 2- Segunda, etc.). Caso seja digitado um valor que não
#  corresponda a um dia da semana, a mensagem “Valor inválido” deve ser exibida na como saída. 


def dia(numero):
   if (numero == 1):
       print("Domingo")
   if (numero == 2):
       print("Segunda")
   if (numero == 3):
       print("Terça")
   if (numero == 4):
       print("Quarta")
   if (numero == 5):
       print("Quinta")
   if (numero == 6):
       print("Sexta")
   if (numero == 7):
       print("Sabado")
   if ((numero != 1) and (numero != 2) and (numero != 3) and \
      (numero != 4) and (numero != 5) and (numero != 6) and (numero != 7)):
       print("Valor invalido")
 
numero = float(input("Digite um numero: "))
dia(numero)





