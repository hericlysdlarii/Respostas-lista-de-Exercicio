#  Faça um Programa que peça uma data no formato dd/mm/aaaa
#  e determine se a mesma é uma data válida
 
data = input("Data: ")
# faz o split e transforma em números
dia, mes, ano = map(int, data.split('/'))
valida = False 
# Meses com 31 dias
if(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
   if(dia<=31):
       valida = True
# Meses com 30 dias
elif( mes==4 or mes==6 or mes==9 or mes==11):
   if(dia<=30):
       valida = True
elif mes==2:
   # Testa se é bissexto
   if (ano%4==0 and ano%400!=0) or (ano%400==0):
       if(dia<=29):
           valida = True
   elif(dia<=28):
           valida = True
 
if(valida == True):
   print('Data válida')
else:
   print('Data Inválida')








