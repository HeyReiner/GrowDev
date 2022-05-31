num1 = float(input("Insira um número: "))
num2 = float(input("Insira outro número: "))
num3 = float(input("Insira mais um número: "))

if num1 > num2 and num1 > num3:
  print("O maior valor entre estes três números é: {}".format(num1))
elif num2 > num1 and num2 > num3:
  print("O maior valor entre estes três números é: {}".format(num2))
elif num3 > num1 and num3 > num2:
  print("O maior valor entre estes três números é: {}".format(num3))
elif num1 == num2 and num1 == num3:
  print("Todos os números são iguais.")