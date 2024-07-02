str = input("enter the string")

def vow(str):
    count = 0 # count, j = 0, 0
    j = 0
    for i in str:
        if i in ('a', 'e', 'i', 'o', 'u'):
            count = count + 1
        else:
            j = j + 1
    return (count, j)

print(vow(str))
