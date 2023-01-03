# 5) Escreva um algoritmo que leia três números fornecidos pelo usuário e mostre
# se a soma de dois deles resulta no terceiro.


print("Digite três números qualquer e veja se a some de dois deles resulta no terceiro.")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 + n2 == n3:
    print("{} + {} = {}. Logo, a soma de dois números resulta no terceiro".format(n1, n2, n3))
elif n1 + n3 == n2:
    print("{} + {} = {}. Logo, a soma de dois números resulta no terceiro".format(n1, n3, n2))
elif n2 + n3 == n1:
    print("{} + {} = {}. Logo, a soma de dois números resulta no terceiro".format(n2, n3, n1))
else:
    print("A soma de dois números não resulta em nenhum terceiro informado.")
