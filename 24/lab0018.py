#Recursion - function call itself
#base condition
#recursive condition / logic

#EG: factorial , sum of digits

num = 5

def factorial(n):
    if n == 0 or n == 1:
        return n
    else:
        return n * factorial(n-1)

print(factorial(5))

def sumofnum(n):
    if n < 10:
        return n
    else:
        return n % 10 + sumofnum(n // 10)

print(sumofnum(12345))