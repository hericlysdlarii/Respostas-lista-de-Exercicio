#  Faça um Programa que pergunte em que turno você estuda. 
#  Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
#  Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" 
#  ou "Valor Inválido!", conforme o caso. 

turno = input("Digite a primeira letra do seu turno: ")
if (turno == 'M'):
   print("Bom dia!")
if (turno == 'V'):
   print("Boa tarde!")
if (turno == 'N'):
   print("Boa noite!")
if((turno != 'M') and (turno != 'V') and (turno != 'N')):
   print("Valor invalido!")



