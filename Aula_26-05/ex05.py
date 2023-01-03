# 5) Faça um algoritmo para ler a quantidade adquirida e o preço unitário de um
# produto.
# a) Calcular e escrever o total

# total = quantidade adquirida * preço unitário
# b) Leia o desconto sobre a compra e calcule.

# total a pagar = total - desconto
# i) Sabendo-se que:
# (1) Se quantidade <= 5 o desconto será de 2%.
# (2) Se quantidade > 5 e quantidade <=10 o desconto será de
# 3%.
# (3) Se quantidade > 10 o desconto será de 5%.

qdade = int(input("Qual a quantidade adiquirida total do produto? "))
preco = float(input("Qual é o preço unitário do produto? R$"))

custoTotal = qdade * preco
print("O preço total sem desconto é R${}".format(custoTotal))

if qdade <= 5:
    desconto = 0.02
elif qdade > 5 and qdade <= 10:
    desconto = 0.03
elif qdade > 10:
    desconto = 0.05

custoDesconto = custoTotal - (custoTotal * desconto)
print("O preço total com desconto é R${:.2f}".format(custoDesconto))
