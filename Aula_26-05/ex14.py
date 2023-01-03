# 14) Faça um algoritmo para ler a temperatura atual e conforme leitura, imprima o
# resultado de acordo com a tabela abaixo.

# Temperatura Resultado
# até 15o Muito frio
# de 16o à 22o Frio
# de 23o à 26o Agradável
# de 27o à 30o Quente
# 31o ou mais Muito quente

temperatura = int(input("Informe a temperatura atual: "))

resultado = ""

if temperatura <= 15:
    resultado = "Muito frio"
elif temperatura >= 16 and temperatura <= 22:
    resultado = "Frio"
elif temperatura >= 23 and temperatura <= 26:
    resultado = "Agradável"
elif temperatura >= 26 and temperatura <= 30:
    resultado = "Quente"
elif temperatura >= 31:
    resultado = "Muito quente"

print("A temperatura agora está {}.".format(resultado))
