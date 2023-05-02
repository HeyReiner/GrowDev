# 6) As reprovações são maiores entre os alunos do 1o, 2o ou 3o ano?. Crie um gráfico para mostrar isso.

import matplotlib.pyplot as plt
from funcoes import carregar

info = carregar('alunos.csv')


def reprovacoes():
    reprovacoes_1ano = reprovacoes_2ano = reprovacoes_3ano = 0
    for linha in info:
        if linha['ano'] == '1' and linha['faltas'] > 15 or (linha['nota exame'] > 0 and linha['nota exame'] <= 5):
            reprovacoes_1ano += 1
        elif linha['ano'] == '2' and linha['faltas'] > 15 or (linha['nota exame'] > 0 and linha['nota exame'] <= 5):
            reprovacoes_2ano += 1
        elif linha['ano'] == '3' and linha['faltas'] > 15 or (linha['nota exame'] > 0 and linha['nota exame'] <= 5):
            reprovacoes_3ano += 1
    return reprovacoes_1ano, reprovacoes_2ano, reprovacoes_3ano


reprovacoes_1ano, reprovacoes_2ano, reprovacoes_3ano = reprovacoes()

print('\nAs reprovações são maiores entre os aludos do 1° ano conforme podemos observar no gráfico a seguir.\n')

eixo_x = ['1° ano', '2° ano', '3° ano']
eixo_y = [reprovacoes_1ano, reprovacoes_2ano, reprovacoes_3ano]

fig, ax = plt.subplots()
ax.bar(eixo_x, eixo_y, color='r', label='Qdade de alunos reprovados')
plt.title('Reprovações por ano')
plt.axis('auto')
plt.legend()
plt.ylabel('Número de alunos')
plt.xlabel('Anos escolares')
plt.show()
