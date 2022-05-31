prod0 = float(input("Qual o preço do primeiro produto? R$"))
prod1 = float(input("Qual o preço do segundo produto? R$"))
prod2 = float(input("Qual o preço do terceiro produto? R$"))
prod3 = float(input("Qual o preço do quarto produto? R$"))
prod4 = float(input("Qual o preço do quinto produto? R$"))

subTotal = prod0 + prod1 + prod2 + prod3 + prod4
valorImposto = subTotal * 6/100
valorTotal = subTotal + valorImposto

print("O subtotal da venda foi de R${}, o valor do imposto é R${}, e o valor total é R${}".format(subTotal, valorImposto, valorTotal))