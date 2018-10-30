import random
aryList = ["cookies", "candy", "coffee"]

for i in range(3):
    choice = input("what else shall I add")
    aryList.append(choice)

#print(aryList)
for i in range(len(aryList)):
    print(aryList[i])
number = random.randint(0,5)
print(aryList[number])