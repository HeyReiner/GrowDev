# 9) Escreva um algoritmo que receba um número e escreva “Par” caso esse
# número seja par e escreva “Impar” caso esse número seja impar

num = int(input("Digite um número para verificar se o mesmo é ímpar ou par: "))

if num % 2 == 0:
    print("O número {} é par.".format(num))
else:
    print("O número {} é ímpar.".format(num))
