# 3) O custo de um carro novo ao consumidor é a soma do custo de fábrica com a
# porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica).
# Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%,
# escrever um algoritmo para ler o custo de fábrica de um carro, calcular e
# escrever o custo final ao consumidor.

custoFabrica = float(input("Digite o custo de fábrica de um carro em R$"))

porcentagemDistribuidor = custoFabrica * 28/100
imposto = custoFabrica * 45/100

custoFinal = custoFabrica + porcentagemDistribuidor + imposto

print("O custo final do carro será de R${:.2f}".format(custoFinal))
