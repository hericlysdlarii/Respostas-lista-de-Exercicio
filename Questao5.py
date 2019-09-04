#  Faça um programa para a leitura de duas notas parciais de um aluno. 
#  O programa deve calcular a média alcançada pelo aluno e apresentar como resultado o seguinte: 
#  
#  a) A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; 
#  b) A mensagem "Reprovado", se a média for menor do que sete; 
#  c) A mensagem "Aprovado com Distinção", se a média for igual a dez. 

nota1 =  float(input("Entre com primeira nota: "))
nota2 =  float(input("Entre com segunda nota: "))
media = (nota1 + nota2) / 2
if ((media < 10) and (media >= 7)):
   print("Aprovado")
if (media < 7):
    print("Reprovado")
if (media == 10):
    print("Aprovado com distinçao")



