#map

num = [1,2,3,4,5]

def double(n):
    return n*2

new_num = map(double,num)
print(list(new_num))

#even number using map
def even(n):
    return  n % 2 == 0
even_list = map(even,num)
print(list(even_list))

#even number using filter - Hence it filters and display only filtered value, Not All

even_filter = filter(even,num)
print(list(even_filter))

#using lamda

even_lamda = map(lambda n:n%2==0,num)
print(list(even_lamda))