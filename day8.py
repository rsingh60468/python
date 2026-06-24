#two sum 

# def sum(list, target):
#      for i in list:
#             for j in list:
#                 if(list[i] + list[j] == target):
#                     emp.append[i]
#                     emp.append[j]
#                     return emp
# sum(nums, 9)

# aproach 2


# nums = [2, 7, 8, 10, 15]
# emp = []

# def sum(list, target):
#      i = 0
#      while i < len(list):
#           j = 0
#           while j < len(list):
#                if (list[i] + list[j] == target):
#                     return [i,j]
#                j += 1
#           i += 1
# print(sum(nums, 9))

#palindrome checker

num = 12345
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

# return (num == rev)
