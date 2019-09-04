#  Faça um programa que lê três notas parciais obtidas por um aluno numa disciplina
#  ao longo de um semestre, e calcule a sua média. 
#  A atribuição de conceitos obedece à tabela abaixo: 

#  Média de Aproveitamento/Conceito:

#     Entre 9.0 e 10.0 → A 
#     Entre 7.5 e 9.0 → B 
#     Entre 6.0 e 7.5 → C 
#     Entre 4.0 e 6.0 → D 
#     Entre 4.0 e zero → E 

#  O programa deve mostrar na tela as notas, a média, o conceito correspondente
#  e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E. 
 
def situaçao(nota1, nota2, nota3):
  
   media = (nota1 + nota2 + nota3) / 3
 
   if ((media >= 9) and (media <= 10)):
       print("\nNotas: ")
       print(nota1, nota2, nota3)
       print("Media: " + str(media))
       print("Cenceito: A")
       print("Aprovado")
   if ((media >= 7.5) and (media < 9)):
       print("\nNotas: ")
       print(nota1, nota2, nota3)
       print("Media: " + str(media))
       print("Cenceito: B")
       print("Aprovado")
   if ((media >= 6) and (media < 7.5)):
       print("\nNotas: ")
       print(nota1, nota2, nota3)
       print("Media: " + str(media))
       print("Cenceito: C")
       print("Aprovado")
   if ((media >= 4) and (media < 6)):
       print("\nNotas: ")
       print(nota1, nota2, nota3)
       print("Media: " + str(media))
       print("Cenceito: D")
       print("Reprovado")
   if ((media >= 0) and (media < 4)):
       print("\nNotas: ")
       print(nota1, nota2, nota3)
       print("Media: " + str(media))
       print("Cenceito: E")
       print("Reprovado")
 
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
situaçao(nota1, nota2, nota3)






