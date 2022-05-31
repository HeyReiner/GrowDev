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
  print("A media das notas {} e {} resultam em {}, que corresponde ao conceito {} e classifica o aluno como APROVADO!".format(n1, n2, media, conceito))
else:
  print("A media das notas {} e {} resultam em {}, que corresponde ao conceito {} e classifica o aluno como REPROVADO!".format(n1, n2, media, conceito))