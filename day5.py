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


i=1
while i<=5:
    if(i==3):
        i+=1 #skip
        continue
    print(i) # this line should exectute after checking if condition
    i+=1