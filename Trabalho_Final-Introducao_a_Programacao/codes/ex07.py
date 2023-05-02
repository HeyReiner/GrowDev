# 7) Qual dos anos (1o, 2o ou 3o) mais procura a monitoria?. Crie um gráfico para mostrar esses dados.
import matplotlib.pyplot as plt
from funcoes import carregar

info = carregar('alunos.csv')

for ano in info:
    ano['ano'] = int(ano['ano'])


def calc_ano_maior_monitoria(ano):
    alunos_monitoria = 0
    for linha in info:
        if linha['ano'] == ano and linha['monitoria'] == 'True':
            alunos_monitoria += 1
    return alunos_monitoria


monitoria_1ano = calc_ano_maior_monitoria(1)
monitoria_2ano = calc_ano_maior_monitoria(2)
monitoria_3ano = calc_ano_maior_monitoria(3)

x = ['1° ano', '2° ano', '3° ano']
y = [monitoria_1ano, monitoria_2ano, monitoria_3ano]

fig, ax = plt.subplots()
ax.bar(x, y, color='g', label='Qdade de alunos que procuraram a monitoria')
plt.title('Procura por monitoria')
plt.axis(ymin=0, ymax=1000)
plt.legend(fontsize='x-small')
plt.ylabel('Número de alunos')
plt.xlabel('Anos escolares')
plt.show()
