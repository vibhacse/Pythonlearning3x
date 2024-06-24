#Vowels [a,e,i,o,u] using filter

characters = ['c','a','e','k','u','i']
vow = ['a','e','i','o','u']

def vowels(num):
    if num in vow:
        return num

print_vow = list(filter(vowels,characters))
print(print_vow)