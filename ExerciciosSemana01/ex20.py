print("Quanto à questão de compra de ações, responda:")
qdadecompradas = int(input("Qual foi a quantidade de ações compradas? "))
valorcompradas = float(input("Qual foi o valor de compra da ação naquele periodo? "))
taxacompra = float(input("Qual foi a taxa paga na compra da ação? "))
print("Quanto à questão de venda de ações, responda:")
qdadevendidas = int(input("Qual foi a quantidade de ações vendidas? "))
valorvendidas = float(input("Qual foi o valor de venda da ação naquele periodo? "))
taxavenda = float(input("Qual foi a taxa paga na venda da ação? "))

valorTaxaCompra = (qdadecompradas * valorcompradas) * taxacompra
valorTotalCompra = (qdadecompradas * valorcompradas) + valorTaxaCompra
valorTaxaVenda = (qdadevendidas * valorvendidas) * taxavenda
valorTotalVenda = (qdadevendidas * valorvendidas) - valorTaxaVenda
valorDiferencaTotal = valorTotalVenda - valorTotalCompra


print("\na) O valor total gasto na compra de ações: R${:.2f}".format(valorTotalCompra))
print("b) O valor pago em taxa durante a compra: R${:.2f}".format(valorTaxaCompra))
print("c) O valor total ganho na venda das ações: R${:.2f}".format(valorTotalVenda))
print("d) O valor pago na venda: R${:.2f}".format(valorTaxaVenda))
print("e) O valor de diferença total entre a compra e a venda: R${:.2f}".format(valorDiferencaTotal))
