
num = int(input("Enter the number:"))

def sum(value):
    return value + value

print(sum(num))

#lambda

list1 = [10,20,30,40]
newlist = list(map(lambda any: any + any, list1))
print(newlist)


