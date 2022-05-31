qdadeDesejada = int(input("Quantos biscoitos você deseja fazer? "))

qdadeacucar = qdadeDesejada * 1.5 / 48
qdademanteiga = qdadeDesejada * 1 / 48
qdadefarinha = qdadeDesejada * 2.75 / 48

print("Os ingredientes necessários para fazer {} biscoitos serão:\n{:.2f} xícaras de açúcar;\n{:.2f} xícaras de manteiga;\n{:.2f} xícaras de farinha.".format(qdadeDesejada, qdadeacucar, qdademanteiga, qdadefarinha))