# 15) Construa um algoritmo que, a partir de duas cores primárias fornecidas pelo
# usuário, determine qual cor seria obtida pela mistura delas. As cores
# vermelho, azul e amarelo são chamadas de cores primárias porque não
# podem ser obtidas a partir de outras cores e, quando misturadas, resultam
# numa cor secundária, de acordo com as seguintes regras:
# a) vermelho + azul = roxo;
# b) vermelho + amarelo = laranja;
# c) azul + amarelo = verde.
# Se o usuário inserir algo diferente de “vermelho”, “azul” ou “amarelo”, o
# programa deverá exibir uma mensagem de erro. Caso contrário, o programa
# deve exibir o nome da cor secundária resultante.

cor1 = str(input(
    "Informe uma cor primária (vermelho, azul ou amarelo) para ser misturada com outra: "))
cor2 = str(input("Informe outra cor primária para a mistura: "))

if cor1 == cor2 or (cor1 != 'azul' and cor1 != 'vermelho' and cor1 != 'amarelo') or (cor2 != 'azul' and cor2 != 'vermelho' and cor2 != 'amarelo'):
    print("Por favor, insira apenas cores primárias e que sejam diferentes umas das outras.")
else:
    if (cor1 == 'vermelho' and cor2 == 'azul') or (cor1 == 'azul' and cor2 == 'vermelho'):
        print("A mistura de {} com {} resulta em roxo!".format(cor1, cor2))
    elif (cor1 == 'azul' and cor2 == 'amarelo') or (cor1 == 'amarelo' and cor2 == 'azul'):
        print("A mistura de {} com {} resulta em verde!".format(cor1, cor2))
    elif (cor1 == 'vermelho' and cor2 == 'amarelo') or (cor1 == 'amarelo' and cor2 == 'vermelho'):
        print("A mistura de {} com {} resulta em laranja!".format(cor1, cor2))
