
# 1. Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.

year = int(input("Enter the Year:"))

if (year%4 == 0) and (year%100 != 0) or (year%400 == 0):
            print("Leap Year")
else:
    print("Not a Leap Year")

# 2. Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides, 
# determine if the triangle is equilateral (all sides are equal), 
# isosceles (exactly two sides are equal), or scalene (no sides are equal).

a = float(input("Enter A Side:"))
b = float(input("Enter B Side:"))
c = float(input("Enter C Side:"))

if (a == b == c):
        print("Triangle is equilateral")
elif (a == b) or (a == c):
        print("Triangle is isosceles")
elif (b == a) or (b == c):
        print("Triangle is isosceles")
else:
        print("Triangle is scalene")

# 3. Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 14

num = int(input("Enter the number:"))
fact = 1
if num > 0:
    for i in range(1, num+1):
        fact = fact * i
    print("The factorial of",num,"is:",fact)
else:
    print("Inalid Number:",num)

#4. Fibonaci series
# 0,0+1, 0+1+1,
# n = 7 
# 0, 1, 2, 3, 5, 8, 13

num = int(input("Enter the number:"))
first = 0
second = 1
for i in range(num):
    print(first)
    temp = first + second
    first = second
    second = temp
