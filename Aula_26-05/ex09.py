# 9) Escreva um programa que peça ao usuário para fornecer um dia, mês e o
# ano arbitrários e determine se esses dados correspondem a uma data válida.
# Não deixe de considerar que existem meses com 30 e 31 dias, e que
# fevereiro pode ter 28 ou 29 dias, dependendo se o ano for bissexto.
# Considere que um ano é bissexto quando for divisível por 4.

dia = int(input("Forneça um dia qualquer: "))
mes = int(input("Forneça um mês qualquer: "))
ano = int(input("Forneça um ano qualquer: "))

if ano % 4 == 0:
    anoBisesto = True
else:
    anoBisesto = False

if mes == 2 and anoBisesto == True:
    diasValidos == 29
elif mes == 2 and anoBissexto == False:
    diasValidos = 28
elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    diasValidos = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    diasValidos = 30
else:
    diasValidos = 0

if dia <= diasValidos and dia >= 1 and mes <= 12 and mes >= 1:
    print("Estes dados correspondem a uma data válida!")
else:
    print("Estes dados não correspondem a uma data válida!")
