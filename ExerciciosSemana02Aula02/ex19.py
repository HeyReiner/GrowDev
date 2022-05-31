numInicial = int(input("Informe um número inteiro menor que 1000 para ter suas quantidades de centenas, dezenas e unidades contadas: "))

aux = numInicial

if aux >= 1000 or aux < 0:
  print("Por favor, insira um número válido dentro dos critérios exigidos.")
else:
  if aux >= 100:
    cent = aux // 100
    aux -= cent * 100
    dez = aux // 10
    aux -= dez * 10
    uni = aux // 1
    print("O número {} contem {} centena(s), {} dezena(s) e {} unidade(s)".format(numInicial, cent, dez, uni))
  elif aux < 100 and aux >= 10:
    dez = aux // 10
    aux -= dez * 10
    uni = aux // 1
    print("O número {} contem {} dezena(s) e {} unidade(s)".format(numInicial, dez, uni))
  elif aux < 10:
    uni = aux // 1
    print("O número {} contem {:} unidade(s)".format(numInicial, uni))