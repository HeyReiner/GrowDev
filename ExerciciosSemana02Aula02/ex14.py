temperatura = int(input("Informe a temperatura atual: "))

resultado = ""

if temperatura <= 15:
  resultado = "Muito frio"
elif temperatura >= 16 and temperatura <= 22:
  resultado = "Frio"
elif temperatura >= 23 and temperatura <= 26:
  resultado = "Agradável"
elif temperatura >= 26 and temperatura <= 30:
  resultado = "Quente"
elif temperatura >= 31:
  resultado = "Muito quente"

print("A temperatura agora está {}.".format(resultado))