# 4) De todos os alunos que reprovaram quantos foram por falta e quantos foram por nota, e quantos foram por ambas as causas?

from funcoes import carregar

info = carregar('alunos.csv')

reprovados_falta = reprovados_nota = 0

for linha in info:
    if linha['faltas'] > 15:
        reprovados_falta += 1
    if linha['nota exame'] <= 5 and linha['nota exame'] > 0:
        reprovados_nota += 1

qdade_reprovados_total = reprovados_falta + reprovados_nota

print(
    f"\033[1;37m{reprovados_falta}\033[m alunos foram reprovados por \033[1;31mFALTA\033[m!")
print(
    f"\033[1;37m{reprovados_nota}\033[m alunos foram reprovados por \033[1;31mNOTA\033[m!")
print(
    f"Logo, \033[1;37m{qdade_reprovados_total}\033[m alunos foram reprovados por \033[1;31mAMBAS\033[m as causas.")
