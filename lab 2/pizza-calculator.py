#Brian Mourik
##Pizza Calculator


print("********************************************")
print("Meatbarn Pizza's, there juicalisious!")
print("********************************************")
print("How many of these would you like?")
small  = float(input("Small chicken coop: "))
medium = float(input("Medium beef supreme: "))
large  = float(input("Large meat slab: "))
print("********************************************")

uitkomst = (((small*6.50)+(medium*8.50))+(large*10.50))

print("Cost= "+ str(round(uitkomst, 2)))