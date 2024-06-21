# List with same and different data type

list1 = [10,20,30,40,50]
list2 = [1,2,"vivek","bharathi",3.14,10]
list3 = [1,2,3,4,5]

print(list1)
print(list2)

print(type(list1))
print(type(list2))

print(list1[0], list1[2], list1[4]) #Limit exceeds the list length, then its out of index error
print(list1[1:3])#multiple index values (from value:to value) in list

print(list1 == list2) #false

print(list1 == list3) #true

print(len(list1))

print(list1*2)

length = len(list1)

result = []

for i in list1:
    result.append(i*2)

print(result)

list4 = list1
print(list4)

list4.append(456)
print(list4)

list4.remove(40)
print(list4)


