cor1 = str(input("Informe uma cor primária (vermelho, azul ou amarelo) para ser misturada com outra: "))
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

