# 4) O programa de fidelidade de uma determinada livraria premia seus clientes
# de acordo com o número de livros comprados a cada mês. Os pontos são
# atribuídos da seguinte forma:
# a) Se um cliente comprar 0 livros, ele ganhará 0 pontos.
# b) Se um cliente comprar um livro, ele ganhará 5 pontos.
# c) Se um cliente comprar dois livros, ele ganhará 15 pontos.
# d) Se um cliente comprar 3 livros, ele ganhará 30 pontos.
# e) Se um cliente comprar 4 ou mais livros, ele ganhará 60 pontos.
# Crie um algoritmo que leia o número de livros comprados por um cliente e
# exiba o número de pontos correspondentes.

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
