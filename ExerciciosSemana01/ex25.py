n = int(input("Digite um número entre 1 e 9 para ver sua tabuada. "))

aux = 1
count = 1

while aux <= 10:
  print("{} x {} = {}".format(n, count, n * count))
  aux = aux + 1
  count = count + 1