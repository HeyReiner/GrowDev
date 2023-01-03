# 2) Faça um algoritmo que receba um valor negativo e retorne o seu valor
# absoluto (ex: recebe -5 e retorna 5)

valor = int(input("Digite um valor qualquer: "))
if valor < 0:
    valor *= -1
print("O valor absoluto deste número é {}".format(valor))
