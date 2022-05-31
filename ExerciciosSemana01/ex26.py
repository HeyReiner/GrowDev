minutos = int(input("Digite uma quantidade de minutos para ser convertida em horas e dias: "))

horas = minutos / 60
dias = minutos / (60 * 24)

print("{} minutos equivalem a {:.1f} horas e é igual a {:.2f} dias.".format(minutos, horas, dias))
