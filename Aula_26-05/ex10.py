# 10) Construa um algoritmo que leia uma data qualquer (dia, mês e ano) e calcule
# a data do próximo dia. Lembre-se que em anos bissextos o mês de fevereiro
# tem 29 dias. Lembre-se que um ano é bissexto quando for divisível por 4.

ia = int(input("Forneça um dia qualquer: "))
mes = int(input("Forneça um mês qualquer: "))
ano = int(input("Forneça um ano qualquer: "))

if ano % 4 == 0:
    anoBissexto = True
else:
    anoBissexto = False

if dia > 31 or mes > 12 or (dia == 29 and anoBissexto == False):
    print("Por favor insira uma data válida!")
else:
    if mes == 2 and anoBissexto == True:
        diasValidos = 29
    elif mes == 2 and anoBissexto == False:
        diasValidos = 28
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        diasValidos = 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        diasValidos = 30

    dia += 1
    if dia > diasValidos:
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            ano += 1

    print("O próximo dia será: dia {} do mês {} de {}.".format(dia, mes, ano))
