#majority in subarray

# nums = [1, 2, 2, 3]
# target = 2
# count = 0
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)+1):
#         print(nums[i:j])
#         if(nums[i:j].count(target) > len(nums[i:j])//2):
#             print(True)
#             count += 1
#         else:
#             print(False)
# print(count)

# nums = [1, 2, 2, 3]
# target = 2
# count = 0

# for i in range(len(nums)):
#     for j in range(i+1, len(nums)+1):
#         sub = nums[i:j]
#         if(sub.count(target) > len(sub)//2):
#             count += 1
# print(count)
##this is ok but giving TLE


nums = [1, 2, 2, 3]
target = 2
count = 0
sub = []
for el in nums:
    if (el == target):
        sub.append(1)
    else:
        sub.append(-1)
print(sub)
for i in range(len(sub)):
    for j in range(i+1, len(sub)+1):
        if sum(sub[i:j]) > 0:
            count +=1
print(count)