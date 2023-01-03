# 4) Escreva um algoritmo para ler uma temperatura em graus Fahrenheit,
# calcular e escrever o valor correspondente em graus Celsius (baseado na
# fórmula abaixo): C/5 = F-32 / 9

f = int(input("Digite a temperatura em graus Fahrenheit para ser convertido em graus Celsius: "))

c = ((f - 32) / 9) * 5

print("{}°F corresponde à {:.0f}°C".format(f, c))