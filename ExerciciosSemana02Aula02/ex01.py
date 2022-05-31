num1 = float(input("Digite um nnúmero: "))
num2 = float(input("Digite outro nnúmero: "))

opcao = int(input("Digite '1' se deseja fazer a soma destes dois números, ou '2' se deseja fazer a subtração: "))

if opcao == 1:
  print("A soma de {} + {} é {}".format(num1, num2, num1 + num2))
elif opcao == 2:
  print("A subtração de {} - {} é {}".format(num1, num2, num1 - num2))
else:
  print("Por favor, insira apenas os números '1' ou '2'.")