# Try and except

print("Start of the program")

try:
    a = int(input("Enter A value:"))
    b = int(input("Enter B value:"))
    result = a/b
    print(result)

except Exception as e:
    print(e)


