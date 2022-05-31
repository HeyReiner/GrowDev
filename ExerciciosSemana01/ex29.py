"""
x = float(input("Digite um valor a ser convertido em uma determinada quantidade de moedas em reais: R$"))

mUm = x // 1
x -= (mUm * 1)

m50 = x // 0.5
x -= (m50 * 0.5)

m25 = x // 0.25
x -= (m25 * 0.25)

m10 = x // 0.1
x -= (m10 * 0.1)

m5 = x // 0.05
x -= (m5 * 0.05)

m1 = x // 0.01
x -= (m1 * 0.01)

print("A conversão dessa quantidade em reais para moedas resulta em: {:.0f} moeda(s) de um real, {:.0f} moeda(s) de cinquenta centavos, {:.0f} moeda(s) de vinte e cinco centavos, {:.0f} moeda(s) de dez centavos, {:.0f} moeda(s) de cinco centavos e {:.0f} moeda(s) de um centavo.".format(mUm, m50, m25, m10, m5, m1))
"""
valor = float(input("Digite um valor em reais a ser convertido em uma determinada quantidade de moedas: R$"))

mUm = valor - valor % 1
valor = valor - mUm

m50 = valor / 0.5
m50 = m50 - m50 % 1
valor = valor - m50 * 0.5

m25 = valor / 0.25
m25 = m25 - m25 % 1
valor = valor - m25 * 0.25

m10 = valor / 0.1
m10 = m10 - m10 % 1
valor = valor - m10 * 0.1

m5 = valor / 0.05
m5 = m5 - m5 % 1
valor = valor - m5 * 0.05

m1 = valor / 0.01 
m1 = m1 - m1 % 1
valor = valor - m1 * 0.01

print("A conversão dessa quantidade em reais para moedas resulta em: {:.0f} moeda(s) de um real, {:.0f} moeda(s) de cinquenta centavos, {:.0f} moeda(s) de vinte e cinco centavos, {:.0f} moeda(s) de dez centavos, {:.0f} moeda(s) de cinco centavos e {:.0f} moeda(s) de um centavo.".format(mUm, m50, m25, m10, m5, m1))