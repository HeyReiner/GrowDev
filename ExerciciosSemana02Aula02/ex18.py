salarioInicial = float(input("Informe o salário do colaborador a receber um aumento. R$"))

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

print("O salário antes de R${:.2f} agora com um percentual de aumento de {:.0f}% que corresponde ao acrécimo de R${:.2f} estará reajustado para R${:.2f}".format(salarioInicial, porcentagem, aumento, salarioFinal))