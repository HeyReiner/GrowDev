print("Programa Poupança:")
p = float(input("Qual o valor da aplicação mensal? R$"))
i = float(input("Qual a taxa de rendimento? "))
n = int(input("Qual o némero de meses? "))

renda = (p * ((1 + i) ** n) - 1) / i

print("A renda obtida com a aplicação de R${:.2f} por {} meses à {:.2f} de taxa é de R${:.2f}".format(p, n, i, renda))