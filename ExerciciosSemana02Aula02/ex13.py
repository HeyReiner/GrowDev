segundos = int(input("Informe a quantidade de segundos desejada: "))

if segundos >= 60 and segundos < 3600:
  minutos = segundos / 60
  print("{} segundos equivale a {:.2f} minutos.".format(segundos, minutos))
elif segundos >= 3600 and segundos < 86400:
  horas = segundos / 3600
  print("{} segundos equivale a {:.2f} horas.".format(segundos, horas))
elif segundos >= 86400:
  dias = segundos / 86400
  print("{} segundos equivale a {:.2f} dias.".format(segundos, dias))