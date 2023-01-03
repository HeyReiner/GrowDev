# 7) Escreva um algoritmo que receba 3 números, faça a soma dos dois primeiros
# e verifique se o resultado da soma é maior que o terceiro número lido.

print("Informe três números para verificar se a soma dos dois primeiros é maior que o terceiro.")
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))
n3 = float(input("Informe o terceiro número: "))

if n1 + n2 > n3:
    print("{} + {} é maior que {}".format(n1, n2, n3))
elif n1 + n2 == n3:
    print("{} + {} é igual a {}".format(n1, n2, n3))
else:
    print("{} + {} não é maior que {}".format(n1, n2, n3))
