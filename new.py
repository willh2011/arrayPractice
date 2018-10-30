#tshirt = ["small", "medium", "large"]
#price = [8, 9, 12]
tshirt = [["small", 8], ["medium", 9], ["large", 12]]
for i in range(len(tshirt)):
    #print(tshirt[i], price[i])
    print(tshirt[i][0])




#string formatting
name = "Fido "
age = 10
#print(name + "is " + str(age) + " years old")
#print("{} is {} years old".format(name, age))
print(f"{name} is {age} years old")