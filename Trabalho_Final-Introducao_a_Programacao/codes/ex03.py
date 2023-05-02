# 3) Quantos alunos do 3o ano reprovaram? e desses quantos procuraram monitoria?

from funcoes import carregar

info = carregar('alunos.csv')

qdade_reprovados = 0

for linha in info:
    if linha['ano'] == '3' and (0 < linha['nota exame'] < 5 or linha['faltas'] > 15):
        qdade_reprovados += 1

print(
    f"\n\033[1;37m{qdade_reprovados}\033[m alunos do 3° ano \033[1;31;40mreprovaram\033[m!")

qdade_reprovados_com_monitoria = 0

for linha in info:
    if (linha['ano'] == '3' and (0 < linha['nota exame'] <= 5 or linha['faltas'] > 15)) and linha['monitoria'] == 'True':
        qdade_reprovados_com_monitoria += 1

print(
    f"Destes, \033[1;37m{qdade_reprovados_com_monitoria}\033[m \033[1;37;40mprocuraram\033[m a monitoria.\n")
