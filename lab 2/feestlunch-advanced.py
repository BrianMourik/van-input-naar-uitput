print("********************************************")
croisants  = float(input("Hoeveel croisants: "))
stokbroden = float(input("hoeveel stokbroden: "))
korting    = float(input("hoe veel kortings bonnen: "))
print("********************************************")

Crcost = 0.39
Stcost = 2.78
Krcost = 0.50

uitkomst = (((stokbroden*Stcost)+(croisants*Crcost))-(korting*Krcost))

print("Cost= "+ str(round(uitkomst, 2)))