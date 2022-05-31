x = int(input("Qual a quantidade de torcedores do time X? "))
y = int(input("Qual a quantidade de torcedores do time Y? "))
z = int(input("Qual a quantidade de torcedores do time Z? "))

total = x + y + z

porcent_x = 100 * x / total
porcent_y = 100 * y / total
porcent_z = 100 * z / total

print("A porcentagem de torcedores do time X é {}%, do time Y {}%, e do time Z {}%".format(porcent_x, porcent_y, porcent_z))
