# 6) Numa determinada escola, os critérios de aprovação são os seguintes:
# a) O aluno deve ter, no máximo, 25% de faltas;
# b) A nota final deve ser igual ou superior a 7,00.
# Construa um algoritmo para ler as notas que um aluno tirou nos 4 bimestres,
# o número total de aulas e o número de faltas, mostrando ao final a situação
# do aluno como sendo “Aprovado”, “Reprovado por Faltas” e “Reprovado por
# média”, considerando que a reprovação por faltas se sobrepõe a reprovação
# por nota.

n1 = float(input("Qual foi a nota no primeiro bimestre do aluno? "))
n2 = float(input("Qual foi a nota no segundo bimestre do aluno? "))
n3 = float(input("Qual foi a nota no terceiro bimestre do aluno? "))
n4 = float(input("Qual foi a nota no quarto bimestre do aluno? "))
aulas = int(input("Qual o número total de aulas? "))
faltas = int(input("Qual o número total de faltas do aluno? "))

media = (n1 + n2 + n3 + n4) / 4
porcentFaltas = (faltas * 100 / aulas)

if porcentFaltas >= 25:
    print("Reprovado por Faltas.")
elif porcentFaltas < 25 and media >= 7:
    print("APROVADO!")
elif porcentFaltas < 25 and media < 7:
    print("Reprovado por média.")

"""
if  porcentFaltas >= 25:
  print("Reprovado por Faltas.")
elif media >= 7:
  print("APROVADO!")
else:
  print("Reprovado por média.")
"""
