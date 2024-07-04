print("Start of the program!")

try:
    list1 = [1,2,3]
    print(list1[1])

except Exception as e:
    #print("Testing")
    print(e)

else:
    print("No Errors")

finally:
    print("End of the program!")