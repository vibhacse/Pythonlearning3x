# OS Modules
#
import os
# import math
#
# print(os.name)
#
print(os.getcwd())
#
# print(os.environ)
#
# # print(math.pi)
#
# print(os.listdir("C:/Users/Vivekananda.B/Pythonlearning3x/June05"))
#
# os.chdir("C:/Users/Vivekananda.B/Pythonlearning3x/June03")

# os.mkdir("Newjune05")

# Create new txt file

# with open('C:/Users/Vivekananda.B/Pythonlearning3x/June05/Newjune05/sample.txt','w') as fp:
#     fp.write("This is first line...")
#     pass

size = os.path.getsize("C:/Users/Vivekananda.B/Pythonlearning3x/June05/Newjune05/sample.txt")
print(size)

if size != 0:
    print("File exist and has content")
else:
    print("File does not exist or no content")
