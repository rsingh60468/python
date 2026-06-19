# print("start of the loop")
# i = 1
# while i<=5:
#     print(i)
#     i+=1
# print("end of the loop")

# i = 5
# while i>=1:
#     print(i)
#     i-=1

# n = int(input("enter a number : "))
# i = 1
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i+=1

# i = 1
# list = []
# while i<=10:
#     print(i**2)
#     list.append(i**2)
#     i+=1
# print(list)

# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("enter number to find : "))
# i = 0
# while i<=len(tup)-1:
#     if(tup[i] == x):
#         print("found at index : ",i)
#     i+=1

# i=1
# while i<=5:
#     print(i)
#     if(i==3):
#         break
#     i+=1


# i=1
# while i<=5:
#     if(i==3):
#         i+=1 #skip
#         continue
#     print(i) # this line should exectute after checking if condition
#     i+=1

# tup = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for el in tup:
#     if(el == 25):
#         print("25 found")
#         break
#     print(el)
# else:
#     print("END") # only execute whrn loop ends completely 

# x = 25
# idx = 0
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# for el in tup:
#     if(el == x):
#         print("found at index : ",idx)
#     idx +=1

# x = range(10)
# print(x)
# print(type(range(10)))

# for el in range(5):
#     print(el) # 0, 1, 2, 3, 4

# for el in range(1, 5):
#     print(el) # 1, 2, 3, 4

# for el in range(1, 5, 2):
#     print(el) # 1, 3

# for i in range(100, 0, -1):
#     print(i)

# n = 7
# for i in range(1, 11):
#     print(n, "*", i, "=", i*n)

# for i in range(5):
#     pass # when no need to do any work in loop
sum = 0
i=0
n=int(input("enter a value : "))
while i<=n:
    sum += i
    i+=1
print(sum)