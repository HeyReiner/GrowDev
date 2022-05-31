custoFabrica = float(input("Digite o custo de fábrica de um carro em R$"))

porcentagemDistribuidor = custoFabrica * 28/100
imposto = custoFabrica * 45/100

custoFinal = custoFabrica + porcentagemDistribuidor + imposto

print("O custo final do carro será de R${:.2f}".format(custoFinal))