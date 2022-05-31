co = float(input("Informe o cateto oposto do triângulo: "))
ca = float(input("Informe o cateto adjacente deste mesmo triângulo: "))

hip = ((co * co) + (ca * ca)) ** 0.5

print("A hipotenusa desse triângulo é: {}".format(hip))