idadeA = int(input("Qual a sua idade em anos? "))
idadeM = int(input("E mais quantos meses? "))
idadeD = int(input("E quantos dias? "))

idadeTotal = idadeA * 365 + idadeM * 31 + idadeD

print("Sua idade apenas em dias é de: {}".format(idadeTotal))
