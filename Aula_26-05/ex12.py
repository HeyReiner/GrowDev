# 12) Uma certa operadora de telefonia móvel cobra R$ 5,00 mensais pelo seu
# plano básico de transmissão de SMS (mensagens de texto), sendo que taxas
# adicionais são cobradas conforme as regras abaixo:
# a) As primeiras 60 mensagens estão incluídas no plano básico;

# b) b. Se o usuário mandar mais de 60 mensagens, cada mensagem
# adicional custará R$ 0.05, até o limite de 180 mensagens.
# c) c. Acima de 180 mensagens, o valor de cada uma delas passa a R$
# 0,10;
# d) d. A soma dos impostos estaduais e federais amonta a 12% do valor
# de cada fatura.
# Com base nessas informações, crie um algoritmo para ler o número total de
# mensagens enviadas por um usuário. Ao final, calcule o valor da conta e
# mostre todos os dados, incluindo o valor da conta com e sem impostos.

mensagens = int(input("Qual o número total de mensagens enviadas? "))

valorFinal = 0

if mensagens <= 60:
    valorFinal = 5
elif mensagens > 60 and mensagens <= 180:
    valorFinal += (mensagens - 60) * 0.05 + 5
else:
    valor_ate_180 = mensagens - 180
    valorFinal = valor_ate_180 * 0.1 + (120 * 0.05) + 5  # 120 pq 180-60 é 120

valorFinalImpostos = valorFinal + (valorFinal * 12/100)

print("Valor final da conta com impostos foi de R${:.2f} e sem impostos foi de R${:.2f}".format(
    valorFinalImpostos, valorFinal))
