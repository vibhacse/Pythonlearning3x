#Filter
#Filter is applicable for List, Tuple and Set
#Allows you to filter the items in list etc

number1 = [1,2,3,4,5,6,7,8]
print(number1)

#even number from list without filter

def even_without_filter(i):
    new_list = []
    for i in number1:
        if i % 2 == 0:
            new_list.append(i)
    print(new_list)
print(even_without_filter(number1))

#even number using filter option
def even_number(n):
    return n % 2 == 0

def odd_number(n):
    return n % 2 != 0

new_even_number = list(filter(even_number,number1))
print(new_even_number)

new_odd_number = list(filter(odd_number,number1))
print((new_odd_number))