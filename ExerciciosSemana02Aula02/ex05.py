qdade = int(input("Qual a quantidade adiquirida total do produto? "))
preco = float(input("Qual é o preço unitário do produto? R$"))

custoTotal = qdade * preco
print("O preço total sem desconto é R${}".format(custoTotal))

if qdade  <= 5:
  desconto = 0.02
elif qdade > 5 and qdade <=10:
  desconto = 0.03
elif qdade > 10:
  desconto = 0.05

custoDesconto = custoTotal - (custoTotal * desconto)
print("O preço total com desconto é R${:.2f}".format(custoDesconto))