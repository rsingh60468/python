height = [1,8,6,2,5,4,8,3,7]
low = 0
max_area = 0
high = len(height)-1
while low < high:
    width = high - low
    area = width * min(height[low], height[high])

    if area > max_area:
        max_area = area
    
    if height[low] <= height[high]:
        low += 1
    else:
        high -= 1
    
print(max_area)