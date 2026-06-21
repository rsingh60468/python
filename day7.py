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