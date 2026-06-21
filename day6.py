#functions

# def calc_sum (num1, num2):
#     sum = num1 + num2
#     # print(sum)
#     return sum

# # calc_sum(5, 6)
# x = calc_sum(5, 6)
# print(x)

# def avg(a, b, c):
#     sum = a + b + c
#     avg = sum/3
#     print(avg)
#     return avg

# avg(3, 4, 6)

# print("ravi", end="&")
# print("singh")

# nums = [1, 2, 3, 4, 5, 6, 7]
# cities = ["delhi", "mumbai", "jaipur", "noida"]
# def length(list):
#     print(len(list))

# length(nums)
# length(cities)

# nums = [1, 2, 3, 4, 5, 6, 7]
# cities = ["delhi", "mumbai", "jaipur", "noida"]
# def lsl(list):
#     for el in list:
#         print(el, end=" ")
#     print("\n")
    
# lsl(nums)
# lsl(cities)

# def calc_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)

# calc_fact(5)
# calc_fact(6)

# def conv(usd):
#     inr = usd*94.43
#     print(usd, "USD =",inr, "INR")

# conv(100)

# def check(num):
#     if(num%2 == 0):
#         print("EVEN")
#     else:
#         print("ODD")
    
# check(47)

# def show(n):
#     if(n ==0):
#         return
#     print(n)
#     show(n-1)
#     print("end", n)

# show(4)

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
    
# print(fact(6))

# def calc_sum(n):
#     if(n==0):
#         return 0
#     else:
#         return calc_sum(n-1)+n
    
# print(calc_sum(10))

# list = [0, 1, 2, 3, 4]
# def list_all(i=0):
#     if(i==len(list)):
#         return 
#     print(list[i])
#     list_all(i+1)

# print(list_all())

def print_list(list, idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits=["mango", "banana", "apple", "litchi"]

print_list(fruits) 