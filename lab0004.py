# + operator for str to concatenate
firstName = input("Enter Your First Name:")
lastName = input("Enter You Last Name:")
fullName = None
print(id(fullName))
fullName = firstName +" "+ lastName
print(r"Your Name is \n here:"+fullName) # r for raw
print(id(fullName))
print(len(fullName)-1)
print(fullName.index(' '))

# + operator for int to sum values
firstNum = int(input("Enter First Number:"))
secondNum = int(input("Enter Second Number:"))
total = firstNum + secondNum
print(total)

#LIST

aList = ['car','bus','van','train']
print(aList)
print(aList[2])
print(aList[-4])
print("No. of Items in List:",len(aList))
name = input("Enter the Names:")
nList = name.split()
print("The Name are added into List:",nList)
nItems = input("Enter new value:")
aList.append(nItems)
print("The list after adding new value:",aList)
aList.insert(2,nItems)
print("Items after Insert:",aList)
aList.reverse()
print("Reverse of Items in List:",aList)
aList.remove(nItems)
print("After remove of new items:",aList)
aList.pop(2)
print("New items after pop:",aList)
bList = aList.copy()
aList.clear()
print("The List are Cleared:",aList)
print("The new List are:",bList)