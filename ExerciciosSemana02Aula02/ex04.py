f = int(input("Digite a temperatura em graus Fahrenheit para ser convertido em graus Celsius: "))

c = ((f - 32) / 9) * 5

print("{}°F corresponde à {:.0f}°C".format(f, c))