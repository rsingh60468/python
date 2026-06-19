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

def conv(usd):
    inr = usd*94.43
    print(usd, "USD =",inr, "INR")

conv(100)