l1 = float(input("Informe o comprimento do primeiro lado do trângulo: "))
l2 = float(input("Informe o comprimento do segundo lado do trângulo: "))
l3 = float(input("Informe o comprimento do terceiro lado do trângulo: "))

triangulo = ''

if l1 == l2 and l2 == l3 and l1 == l3:
  triangulo = 'equilátero'
elif (l1 == l2 and l1 != l3 and l2 != l3) or (l3 == l1 and l3 != l2 and l1 != l2) or (l2 == l3 and l2 != l1 and l3 != l1):
  triangulo = 'isóceles'
elif l1 != l2 and l2 != l3 and l1 != l3:
  triangulo = 'escaleno'

print("Um triângulo de medidas {}x{}x{} é considerado um triângulo {}.".format(l1, l2, l3, triangulo))