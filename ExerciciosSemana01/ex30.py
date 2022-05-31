print("Digite um valor numérico de até 3 digitos: ")
numeroInicial = int(input())

centenas = numeroInicial // 100
aux = numeroInicial - (100 * centenas)
dezenas = aux // 10
aux = aux - (10 * dezenas)
unidades = aux // 1

print("O número {} tem {} centenas, {} dezenas e {} unidades.".format(numeroInicial, centenas, dezenas, unidades))
