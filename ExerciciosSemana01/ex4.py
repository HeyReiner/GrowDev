num1 = float(input("Digite um número a ser somado: "))
num2 = float(input("Digite outro número: "))
num3 = float(input("Digite um número que dividirá a soma: "))

result = (num1 + num2) / num3

print("O resultado da soma de ({} + {}) dividido por {} é: {}".format(num1, num2, num3, result))