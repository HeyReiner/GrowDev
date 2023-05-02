import csv


def carregar(nome_arquivo):
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

    return info
