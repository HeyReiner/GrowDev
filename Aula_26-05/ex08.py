# 8) Um carpinteiro esculpe placas personalizadas para estabelecimentos
# comerciais e deseja um programa que faça orçamentos das placas que
# produz, considerando as seguintes informações:
# a) O valor mínimo de qualquer placa é de R$ 300,00;
# b) Placas de angelim custam R$ 150,00 adicionais, mas placas de pinus
# não possuem nenhum custo extra;
# c) Frases com até 12 caracteres estão incluídas no valor mínimo; para
# frases maiores, são cobrados R$ 15,00 por caractere;

# d) Para placas com dizeres brancos ou pretos não se cobra adicional,
# mas se ele contiver letras douradas, cobra-se R$ 60,00 a mais.
# Baseado nessas informações, construa um algoritmo que leia o número de
# um orçamento, o nome do cliente, tipo de madeira (angelim ou pinus),
# número de caracteres da mensagem e a cor dos caracteres (branco, preto ou
# dourado). Ao final, imprima todos os dados de entrada e o preço da placa
# orçada.

idOrcamento = int(input("Qual o número do orçamento? "))
nome = str(input("Qual o nome do cliente? "))
madeira = str(
    input("Digite (em letras minúsculas) o tipo de madeira : Angelim ou pinus? "))
if (madeira != "angelim" and madeira != "pinus"):
    while (madeira != "angelim" and madeira != "pinus"):
        madeira = str(input("Por favor insira um tipo de madeira válido: "))
nCaracteres = int(input("Qual o número de caracteres da mensagem? "))
corCaracteres = str(input(
    "Insira (em letras minúsculas) a cor dos caracteres: Branco, Preto ou Dourado? "))
if (corCaracteres != "branco" and corCaracteres != "preto" and corCaracteres != "dourado"):
    while (corCaracteres != "branco" and corCaracteres != "preto" and corCaracteres != "dourado"):
        corCaracteres = str(input("Por favor insira um tipo de cor válida: "))

vFinal = 300

if madeira == "angelim":
    vFinal += 150
if nCaracteres > 12:
    vFinal += (nCaracteres - 12) * 15
if corCaracteres == "dourado":
    vFinal += 60

print("O pedido de número {}, em nome de {}, com madeira do tipo {}, contendo {} caracteres de cor {} terá preço final orçado em R${:.2f}".format(
    idOrcamento, nome, madeira, nCaracteres, corCaracteres, vFinal))
