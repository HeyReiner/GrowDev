# 18)As Organizações XTC resolveram dar um aumento de salário aos seus
# colaboradores e lhe contrataram para desenvolver o programa que calcula os
# reajustes. Faça um programa que recebe o salário de um colaborador e o
# reajuste segundo o seguinte critério, baseado no salário atual:
# a) salários até R$ 280,00 (incluindo): aumento de 20%
# b) salários entre R$ 280,00 e R$ 700,00: aumento de 15%
# c) salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
# d) salários de R$ 1500,00 em diante: aumento de 5%
# Após o aumento ser realizado informe na tela:
# a) o salário antes do reajuste;

# b) o percentual de aumento aplicado;
# c) o valor do aumento;
# d) o novo salário, após o aumento.

salarioInicial = float(
    input("Informe o salário do colaborador a receber um aumento. R$"))

if salarioInicial <= 280:
    porcentagem = 20/100
    aumento = salarioInicial * porcentagem
elif salarioInicial > 280 and salarioInicial <= 700:
    porcentagem = 15/100
    aumento = salarioInicial * porcentagem
elif salarioInicial > 700 and salarioInicial <= 1500:
    porcentagem = 10/100
    aumento = salarioInicial * porcentagem
elif salarioInicial > 1500:
    porcentagem = 5/100
    aumento = salarioInicial * porcentagem

salarioFinal = salarioInicial + aumento
porcentagem *= 100

print("O salário antes de R${:.2f} agora com um percentual de aumento de {:.0f}% que corresponde ao acrécimo de R${:.2f} estará reajustado para R${:.2f}".format(
    salarioInicial, porcentagem, aumento, salarioFinal))
