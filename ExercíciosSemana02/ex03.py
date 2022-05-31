valorAquisicao = float(input("Qual o valor de aquisição do produto? R$"))

if valorAquisicao < 50.00:
  valorVenda = valorAquisicao + valorAquisicao * 0.45
else:
  valorVenda = valorAquisicao + valorAquisicao * 0.3

print("O valor de venda desse produto deve ser de: R${:.2f}".format(valorVenda))