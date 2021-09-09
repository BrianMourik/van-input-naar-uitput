print("********************************************")
people = float(input("With how many are you: "))
ingang = float(input("Entrance fee: "))
vip    = float(input("VIP Game fee: "))
time   = float(input("Time spend playing the VIP game: "))
print("********************************************")

uitkomst = ((ingang+(vip*(time/5)))*people)

print("Cost= "+ str(round(uitkomst, 2)))