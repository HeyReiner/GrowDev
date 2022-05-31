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