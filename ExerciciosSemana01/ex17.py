n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))
n3 = float(input("Digite a terceira nota do aluno: "))

peso1 = float(input("Informe o peso da primeira nota em porcentagem "))
peso2 = float(input("Informe o peso da segunda nota em porcentagem "))
peso3 = float(input("Informe o peso da terceira nota em porcentagem "))

media = n1 * peso1 / 100 + n2 * peso2 / 100 + n3 * peso3 / 100

print("A nota final do aluno foi: {}".format(media))