a = float(input("Digite um valor para a variável A: "))
b = float(input("Digite um valor para a variável B: "))

aux = a
a = b
b = aux

print("Após a troca de valores, agora a variável A é {}, e a variável B é {}.".format(a, b))