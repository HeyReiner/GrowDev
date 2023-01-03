# Crie um algoritmo que funcione como um jogo de loteria, conforme as seguintes regras:
# a) O algoritmo deve gerar três números aleatórios entre 0 e 9;
# b) O usuário deve fornecer um palpite com três números, também entre 0 e 9;
# c) Cada um dos palpites do usuário deve ser comparado com os números aleatórios, de acordo com a tabela abaixo:

# Números Correspondentes                                               Número de pontos
# Nenhum número coincidente                                             0
# Acertar um número                                                     10
# Acertar dois números                                                  100
# Acertar os três números, mas não na mesma ordem em que foram gerados  1000
# Acertar três números na mesma ordem que os números aleatórios         1.000.000

from random import randint

n1 = randint(0, 9)
n2 = randint(0, 9)
n3 = randint(0, 9)

print(n1, n2, n3)

a1 = int(input("Informe o primeiro número do palpite: "))
a2 = int(input("Informe o segundo número do palpite: "))
a3 = int(input("Informe o terceiro número do palpite: "))

if n1 == a1 and n2 == a2 and n3 == a3:
    print("Acetou todos os números em ordem e ganhou 1000000 pontos!")
else:
    # não estão em ordem
    a1_hit = a1 == n1 or a1 == n2 or a1 == n3
    a2_hit = a2 == n1 or a2 == n2 or a2 == n3
    a3_hit = a3 == n1 or a3 == n2 or a3 == n3

    acertos = 0

    if a1_hit:
        acertos += 1
    if a2_hit:
        acertos += 1
    if a3_hit:
        acertos += 1

    if acertos == 3:
        print("\nAcertou todos os números mas não em ordem e ganhou 1000 pontos\n")
    elif acertos == 2:
        print("Acertou dois números e ganhou 100 pontos")
    elif acertos == 1:
        print("Acertou um número e ganhou 10 pontos")
    else:
        print("Não acertou nenhum número.")
