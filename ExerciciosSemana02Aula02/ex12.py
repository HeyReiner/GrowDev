mensagens = int(input("Qual o número total de mensagens enviadas? "))

if mensagens < 60:
  valorFinal = 5
elif mensagens > 60 and mensagens < 180:
  valorFinal += (mensagens - 60) * 0.05 + 5
elif mensagens > 180:
  valor_ate_180 = mensagens - 180
  valorFinal = valor_ate_180 * 0.1 + (180 * 0.05) + 5

valorFinalImpostos = valorFinal + (valorFinal * 12/100) 

print("Valor final da conta com impostos foi de R${:.2f} e sem impostos foi de R${:.2f}".format(valorFinalImpostos, valorFinal))