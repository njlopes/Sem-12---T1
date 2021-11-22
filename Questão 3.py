popA = int(input())
popB = int(input())
anos = 0
cresA = 0.02
cresB = 0.03
if popB > popA:
        popA, popB = popB, popA
if popA > popB:
    while(popA > popB):
        popA = popA + (popA * cresA)
        popB = popB + (popB * cresB)
        anos += 1
    

print(anos)
