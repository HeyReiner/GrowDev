import math

x = float(input("Quam a posição do primeiro ponto em cm? "))
y = float(input("Quam a posição do segundo ponto em cm? "))

hip = ((x * x) + (y * y)) ** 0.5

print("A distância entre o primeiro ponto e o segundo ponto é: {}cm".format(hip))
