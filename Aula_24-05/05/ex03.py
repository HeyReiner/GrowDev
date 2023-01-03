# 3) Um brechó revende produtos usados, e fixa o preço de venda de cada
# produto conforme o valor de sua aquisição. Se o preço de aquisição de um
# produto é menor do de R$ 50.00, ele deve ser vendido por um preço 45%
# maior; caso contrário, o lucro será de 30%. Sabendo disso, construa um
# algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de
# venda.


valorAquisicao = float(input("Qual o valor de aquisição do produto? R$"))

if valorAquisicao < 50.00:
    valorVenda = valorAquisicao + valorAquisicao * 0.45
else:
    valorVenda = valorAquisicao + valorAquisicao * 0.3

print(
    "O valor de venda desse produto deve ser de: R${:.2f}".format(valorVenda))
