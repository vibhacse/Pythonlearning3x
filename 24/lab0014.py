#dictionary

my_dic = {
"name" : "vivek",
"age" : "28-12-1989"
}

print(my_dic)

num = {
    "a":10,
    "b":20,
    "c":30
}

for k,v in num.items():
    if k == "c":
        print("C is present")
    if v == 10:
        print("Value of A is:",v)

output = 'b' in num
print(output)
print('k' in num)
print('a' in num)