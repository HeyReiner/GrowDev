# 7) Após construir o algoritmo anterior, crie mais duas versões dele para prever
# as seguintes situações:
# a) Um aluno pode ficar em recuperação se possuir frequência suficiente
# (superior a 75%) e média superior a 5 mas inferior a 7;
# b) Caso um aluno reprove por média e faltas, sua situação deve ser
# “Reprovado por Média e Faltas” (ao invés de simplesmente
# “Reprovado por Faltas” como antes).

n1 = float(input("Qual foi a nota no primeiro bimestre do aluno? "))
n2 = float(input("Qual foi a nota no segundo bimestre do aluno? "))
n3 = float(input("Qual foi a nota no terceiro bimestre do aluno? "))
n4 = float(input("Qual foi a nota no quarto bimestre do aluno? "))
aulas = int(input("Qual o número total de aulas? "))
faltas = int(input("Qual o número total de faltas do aluno? "))

media = (n1 + n2 + n3 + n4) / 4
porcentFaltas = (faltas * 100 / aulas)

if porcentFaltas <= 25 and media > 5 and media < 7:
    print("Recuperação.")
elif porcentFaltas >= 25 and media <= 5:
    print("Reprovado por média e por faltas.")
elif porcentFaltas >= 25:
    print("Reprovado por Faltas.")
elif porcentFaltas < 25 and media >= 7:
    print("APROVADO!")
elif porcentFaltas < 25 and media < 7:
    print("Reprovado por média.")
