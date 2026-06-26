# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt", "r")
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# f.close()

# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# line1 = f.readline() #the file is already readed and pointer is at last so this will do no work 
# print(line1)
# line2 = f.readline() #after reading 1st line the pointer stops at end of 1st line. when we again use readline it starts form there 
# print(line2)
# f.close()


# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# again = f.read() # file can only be read once 
# print(again)

# f = open("demo.txt", "w") #overwites previous data
# f.write("this is a new data\n")

# f = open("demo.txt", "a")
# f.write("this is new line")

# f = open("sample.txt", "w") #creates new file if not already exists
# f.close()

#with syntex

# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt","w") as f:
#     f.write("new data")

# f = open("sample.txt", "w") #creates new file if not already exists
# f.close()

# import os
# os.remove("tempCodeRunnerFile.py")

# f = open("practice.txt","w")
# f.write("Hi everyone \nwe are learning file I/O \nusing Java \nI like programming in Java")

# with open("practice.txt", "r")as f:
#     data = f.read()

# new_data = data.replace("Java", "python")
# print(new_data)

# with open("practice.txt", "w")as f:
#     data = f.write(new_data)

# word = "learning"
# with open("practice.txt", "r")as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")


# f = open("practice.txt", "r")
# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r"):
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1

# check_for_line()

count = 0
with open("nums.txt", "r") as f :
    data = f.read()
    print(data)

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)    