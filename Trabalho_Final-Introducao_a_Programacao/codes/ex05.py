# 5) Qual a média de todas as notas (do 1o e 2o semestre) dos alunos do 2o ano?

from funcoes import carregar

info = carregar('alunos.csv')


def media_2ano():
    soma_notas = 0
    count = 0
    for linha in info:
        if linha['ano'] == '2':
            count += 1
            soma_notas += (linha['nota1'] + linha['nota2']) / 2
    media_notas = soma_notas / count
    return media_notas


media_notas = media_2ano()

print(
    f"A \033[1;37mmédia\033[m de todas as notas dos alunos do 2° ano é \033[1;32m{media_notas:.2f}\033[m")
