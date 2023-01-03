# 11) Crie um algoritmo para um jogo de adivinhação, onde o usuário tenta
# adivinhar um número aleatório gerado pelo computador. Esse número
# aleatório é inteiro e não negativo, e deve ser escolhido dentro de uma faixa
# estabelecida pelo usuário (por exemplo, o usuário pode estipular que esse
# número varie entre 0 e 10 ou entre 22 e 48, por exemplo). Após o usuário
# tentar adivinhar qual foi o número gerado, o algoritmo deve escrever esse
# número e dizer se indicar se o palpite do jogador estava correto, muito alto ou
# muito baixo.
# Dica: Para gerar um número aleatório utilize a função randint do módulo
# random.

from random import randint

print("JOGO DA ADIVINHAÇÃO")
a = int(input("Digite um número inteiro e não negativo que servirá como o primeiro número da faixa: "))
b = int(input("Digite outro número sob as mesmas condições que servirá como o ultimo número da faixa: "))

nUsuario = int(input("Digite o número que você acha que será sorteado: "))
nPC = randint(a, b)

if nUsuario == nPC:
    print("PARABÉNS, você acertou o número sorteado")
else:
    print("Você errou, o número sorteado na faixe entre {} e {} foi o {}.".format(a, b, nPC))
