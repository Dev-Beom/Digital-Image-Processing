cheesePrice = 3000
tunaPrice = 3500
specialPrice = 4000

cheeseCount = 0
tunaCount = 0
specialCount = 0

total = 0

selectedIndex = 0

for i in range(0, 5):
    selectedIndex = int(input())
    if selectedIndex == 1:
        cheeseCount += 1
        total += cheesePrice
    elif selectedIndex == 2:
        tunaCount += 1
        total += tunaPrice
    elif selectedIndex == 3:
        specialCount += 1
        total += specialPrice
    else:
        break

    if total >= 15000:
        break

print("Cheese %d Tuna %d Special %d" % (cheeseCount, tunaCount, specialCount))
print("Total = %d" % total)