livrosComprados = int(input("Quantos livros o cliente comprou neste mês? "))

if livrosComprados == 0:
  pontos = 0
elif livrosComprados == 1:
  pontos = 5
elif livrosComprados == 2:
  pontos = 15
elif livrosComprados == 3:
  pontos = 30
elif livrosComprados >= 4:
  pontos = 60

print("O número de pontos que esse tem é {} pontos.".format(pontos))
