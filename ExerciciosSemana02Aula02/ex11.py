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