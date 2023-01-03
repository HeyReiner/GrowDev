# 20) Faça um programa que leia as duas notas parciais obtidas por um aluno
# numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição
# de conceitos obedece à tabela abaixo:
# Média de Aproveitamento
# Entre 9.0 e 10.0 Conceito A
# Entre 7.5 e 8.9 B
# Entre 6.0 e 7.4 C
# Entre 4.0 e 5.9 D
# Entre 0 e 3.9 E

# O algoritmo deve mostrar na tela as notas, a média, o conceito
# correspondente e a mensagem:
# a) APROVADO se o conceito for A, B ou C.
# b) REPROVADO se o conceito for D ou E.

n1 = float(input("Digite a primeira nota parcial do aluno: "))
n2 = float(input("Digite a segunda nota parcial do aluno: "))

media = (n1 + n2) / 2

if media >= 9:
    conceito = 'A'
elif media < 9 and media >= 7.5:
    conceito = 'B'
elif media < 7.5 and media >= 6:
    conceito = 'C'
elif media < 6 and media >= 4:
    conceito = 'D'
elif media < 4:
    conceito = 'E'

if conceito == 'A' or conceito == 'B' or conceito == 'C':
    print("A media das notas {} e {} resultam em {}, que corresponde ao conceito {} e classifica o aluno como APROVADO!".format(
        n1, n2, media, conceito))
else:
    print("A media das notas {} e {} resultam em {}, que corresponde ao conceito {} e classifica o aluno como REPROVADO!".format(
        n1, n2, media, conceito))
