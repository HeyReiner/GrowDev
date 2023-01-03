# 8) Crie um algoritmo para uma empresa de transportes que, a partir do peso de
# uma encomenda fornecida pelo usuário, calcule o preço da remessa
# conforme a seguinte tabela:
# Peso da encomenda Valor
# 500 gramas ou menos R$ 1,10
# Mais de 500 gramas, mas não mais que 2 quilos R$ 2,20
# Mais de 2 quilos, mas não mais de 10 quilos R$ 3,70
# Mais de 10 quilos R$ 5,00 mais R$ 3,80/kg pelo peso que ultrapassar 10 Kg

peso = float(input("Qual o peso da encomenda em Kg? "))

if peso <= 0.5:
  valor = 1.10
elif peso > 0.5 and peso <= 2:
  valor = 2.20
elif peso > 2 and peso <= 10:
  valor = 3.70
else:
  valor = 5 + (peso - 10) * 3.80

print("O valor da remessa para o transporde de uma encomenda de {}Kg será de R${:.2f}".format(peso, valor))