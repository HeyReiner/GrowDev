idOrcamento = int(input("Qual o número do orçamento? "))
nome = str(input("Qual o nome do cliente? "))
madeira = str(input("Digite (em letras minúsculas) o tipo de madeira : Angelim ou pinus? "))
if (madeira != "angelim" and madeira != "pinus"):
  while (madeira != "angelim" and madeira != "pinus"):
    madeira = str(input("Por favor insira um tipo de madeira válido: "))
nCaracteres = int(input("Qual o número de caracteres da mensagem? "))
corCaracteres = str(input("Insira (em letras minúsculas) a cor dos caracteres: Branco, Preto ou Dourado? "))
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

print("O pedido de número {}, em nome de {}, com madeira do tipo {}, contendo {} caracteres de cor {} terá preço final orçado em R${:.2f}".format(idOrcamento, nome, madeira, nCaracteres, corCaracteres, vFinal))
