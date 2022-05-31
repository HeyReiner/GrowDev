pFrances = 0.75
pDoce = 0.85
quindim = 1.50

qdade_pFrances = int(input("Quantos pães franceses foram vendidos hoje? "))
qdade_pDoce = int(input("Quantos pães doces foram vendidos hoje? "))
qdade_quindim = int(input("Quantos quindins foram vendidos hoje? "))

totalFaturado = qdade_pFrances * pFrances + qdade_pDoce * pDoce + qdade_quindim * quindim

print("O total faturado hoje foi de: R${}".format(totalFaturado))

#Modificação 1
"""
pFrances = float(input("Qual o preço do pão frances? "))
pDoce = float(input("Qual o preço do pão doce? "))
quindim = float(input("Qual o preço do quintim? "))

qdade_pFrances = int(input("Quantos pães franceses foram vendidos hoje? "))
qdade_pDoce = int(input("Quantos pães doces foram vendidos hoje? "))
qdade_quindim = int(input("Quantos quindins foram vendidos hoje? "))

totalFaturado = qdade_pFrances * pFrances + qdade_pDoce * pDoce + qdade_quindim * quindim

print("O total faturado hoje foi de: R${}".format(totalFaturado))
"""

#Modificação 2
"""
pFrances = 0.75
pDoce = 0.85
quindim = 1.50

qdade_pFrances = int(input("Quantos pães franceses foram vendidos hoje? "))
qdade_pDoce = int(input("Quantos pães doces foram vendidos hoje? "))
qdade_quindim = int(input("Quantos quindins foram vendidos hoje? "))

totalFaturado = qdade_pFrances * pFrances + qdade_pDoce * pDoce + qdade_quindim * quindim
valorPoupado = (totalFaturado * 10/100)

print("O total faturado hoje foi de: R${}, e R${} desse valor deve ser poupado.".format(totalFaturado, valorPoupado))
"""

#Modificação 3
"""
pFrances = 0.75
pDoce = 0.85
quindim = 1.50

qdade_pFrances = int(input("Quantos pães franceses foram vendidos hoje? "))
qdade_pDoce = int(input("Quantos pães doces foram vendidos hoje? "))
qdade_quindim = int(input("Quantos quindins foram vendidos hoje? "))

totalFaturado = (qdade_pFrances * pFrances + qdade_pDoce * pDoce + qdade_quindim * quindim)
totalComImposto = totalFaturado - (totalFaturado * 5/100)
valorPoupado = (totalComImposto * 10/100)

print("O total faturado hoje, com os impostos já descontados, foi de: R${}\nE R${} desse valor deve ser poupado.".format(totalComImposto, valorPoupado))
"""