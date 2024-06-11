#1. Explain the difference between the = operator and the == operator in Python.
#ANS: = used for assignment of literals and == used for comparison

a = 2
b = 2
print(a == b) #ANS: True

#2. ** operator 
x = 2
y = 5
print(x**y) #ANS: 32 (x power of y)

#3. What does the ^ operator do in Python, and in what context is it commonly used?

print(10 & 12) #Bitwise AND
print(10 | 12) #Bitwise OR
print(10 ^ 12) #Bitwise XOR

a = {10,20,30,20,40,50,60}
print(a) #Set remove duplicate values

name1 = input("Enter first person name:")
age1 = input("Enter first person age:")
name2 = input("Enter first person name:")
age2 = input("Enter secondar person age:")
print("The elder is:",name1) if age1 > age2  else print("The elder is:",name2)
