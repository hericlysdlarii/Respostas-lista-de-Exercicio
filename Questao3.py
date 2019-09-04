#  Faça um Programa que verifique se uma letra digitada é "F" ou "M", 
#  representando o sexo de uma pessoa. Conforme a letra digitada exibir 
#  na tela: F - Feminino, M - Masculino, Sexo Inválido. 

letra = str(input("Sexo: "))
if (letra == 'F'):
    print("Feminino")
if (letra == 'M'):
    print("Masculino")
if ((letra != 'F') and (letra != 'M')):
    print("Sexo Invalido")


