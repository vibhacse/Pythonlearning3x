try:
    #with open("/Users/Vivekananda.B/OneDrive - Brillio/Documents/Bharathi/Automation Testing/sample.txt") as file:
    with open("/Users/Vivekananda.B/OneDrive - Brillio/Documents/Bharathi/Automation Testing/samplesample.txt") as file1:
        content = file1.readline()
        print(content)
except FileNotFoundError as e:
    print(e)
finally:
    print("The End...")

#To write on the file "sample.txt"

try:
    #with open("/Users/Vivekananda.B/OneDrive - Brillio/Documents/Bharathi/Automation Testing/sample.txt") as file2:
    file2 = open("/Users/Vivekananda.B/OneDrive - Brillio/Documents/Bharathi/Automation Testing/sample.txt",'w')
    file2.write("\nTesting Write\n")

except Exception as e:
    print(e)