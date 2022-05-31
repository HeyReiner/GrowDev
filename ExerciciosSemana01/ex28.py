n1 = float(input("Insira um valor: "))
n2 = float(input("Insira outro valor: "))
n3 = float(input("Insira um terceiro valor: "))

somaDecimal = n1 % 1 + n2 % 1 + n3 % 1

print("A soma dos valores decimais dos números {}, {} e {} é {:.2f}".format(n1, n2, n3, somaDecimal))