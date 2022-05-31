print("Considerando a equação de segundo grau ax^2 + bx + c\n")
a = float(input("Qual o valor de a? "))
b = float(input("Qual o valor de b? "))
c = float(input("Qual o valor de c? "))

delta = (b * b) - (4 * a * c)

x1 = (-b + (delta ** 0.5)) / (2 * a)
x2 = (-b - (delta ** 0.5)) / (2 * a)

print("As raizes dessa equação de segundo grau são: {:.2f} e {:.2f}".format(x1, x2))
