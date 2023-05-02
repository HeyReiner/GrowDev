# 1) Quantos alunos estudam em cada escola, e qual a escola com mais alunos?

import csv

nome_arquivo = 'alunos.csv'
arquivo = open(nome_arquivo, encoding='utf-8')
dados = csv.reader(arquivo, delimiter=',')
dados = list(dados)

qdade_dados = len(dados)

info = []

for i in range(1, qdade_dados):
    info.append(
        {
            'nome': dados[i][0],
            'ano': dados[i][1],
            'escola': dados[i][2],
            'nota1': float(dados[i][3]),
            'nota2': float(dados[i][4]),
            'faltas': int(dados[i][5]),
            'nota exame': float(dados[i][6]),
            'monitoria': dados[i][7]
        }
    )

alunos_por_escola = {}

for linha in info:
    chave = linha['escola']
    if chave not in alunos_por_escola:
        alunos_por_escola[chave] = 0
    alunos_por_escola[chave] += 1

print()

for escola in alunos_por_escola.items():
    print(
        f"\033[1;37m{escola[1]}\033[m alunos estudam na escola \033[1;37;40m{escola[0]}\033[m.")

escola_mais_alunos = {
    'escola': '',
    'qdade_alunos': 0
}

for i in alunos_por_escola.items():
    if i[1] > escola_mais_alunos['qdade_alunos']:
        escola_mais_alunos['qdade_alunos'] = i[1]
        escola_mais_alunos['escola'] = i[0]

print(
    f"\nLogo, a escola que mais contém aulos é a \033[1;31;40m{escola_mais_alunos['escola']}\033[m.\n")
