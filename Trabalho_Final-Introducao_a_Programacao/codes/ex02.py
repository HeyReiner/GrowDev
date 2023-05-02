# 2) Quantos alunos do 1o ano foram aprovados sem exame?

from funcoes import carregar

info = carregar('alunos.csv')

qdade_alunos = 0

for linha in info:
    if linha['ano'] == '1' and linha['nota exame'] == 0 and linha['faltas'] >= 15:
        qdade_alunos += 1

print(
    f'\nA quantidade de alunos do 1° ano que foram aprovados \033[1;37msem exame\033[m foi: \033[0;32;40m{qdade_alunos}\033[m\n')
