qdadeComprada = int(input("Informe a quantidade comprada do produto: "))

valorTotal = qdadeComprada * 5.40
qdadeCentanas = qdadeComprada // 100
desconto = (valorTotal * (0.05 * qdadeCentanas))
valorTotalDesconto = valorTotal - desconto

print("O valor total da compra (sem desconto) foi de R${:.2f}.\nA quantidade de centenas compradas desse produto foi {}.\nO desconto foi de R${:.2f}.\nE o valor final da compra (com desconto) foi R${:.2f}".format(valorTotal, qdadeCentanas, desconto, valorTotalDesconto))