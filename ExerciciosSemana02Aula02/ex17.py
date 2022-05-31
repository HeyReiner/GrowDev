conversao = int(input("Digite '1' se você gostaria de passar uma temperatura de Fahrenheit para Celsius, ou '2' se deseja transformar Celsius em Fahrenheit. "))

if conversao == 1:
  tempF = int(input("Informe a temperatura em Fahrenheit: "))
  tempC = (tempF - 32) / 9 * 5
  print("{:.0f}°F corresponde a {:.0f}°C".format(tempF, tempC))
elif conversao == 2:
  tempC = int(input("Informe a temperatura em Celsius: "))
  tempF = tempC * 9 / 5 + 32
  print("{:.0f}°C corresponde a {:.0f}°F".format(tempC, tempF))
else:
  print("Por favor insira um número válido. ('1' ou '2')")
