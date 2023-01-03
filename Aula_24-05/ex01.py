#Considere as variáveis abaixo, inicializadas como segue:
numero1 = 300
numero2 = 100
numero3 = 5
string1 = "Rinoceronte"
string2 = "Zebra"
string3 = "bug”

numero1 == numero3 #False
numero1 > numero3 #True
numero2 < numero3 #False
numero1 == string1 #False
numero1 == "Um" #Ilegal / False
numero1 == "Trezentos" #Ilegal / False
numero1 == "300" #Ilegal / False
string2 == "Dois" #False
string1 == "Rinoceronte" #True
string3 != "Rinoceronte" #True
string3 != "Rinoceronte" or numero1 > 1000 #True
numero2 <= numero1 / 3 #True
numero1 >= 200 #True
numero1 >= numero2 + numero3 #True
numero1 > numero2 and numero1 < numero3 #False
numero1 == 100 or numero1 > numero3 #True
numero1 < 10 or numero3 > 10 #False
numero1 == 30 and numero2 == 100 or numero3 == 100 #False