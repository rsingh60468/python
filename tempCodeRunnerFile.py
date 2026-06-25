seen = set()
def sq(num):
    if(num == 1):
        return True
    arr = []
    while num > 0:
        arr.append(num % 10)
        num = num // 10
    
    for el in arr:
        num = num + (el**2)

    # seen = set()
    if num in seen:
        return False

    seen.add(num)
    # before = len(seen)
    # seen.add(num)

    # if len(seen) == before:
    #     return False
    
    return sq(num)

ans = sq(19)
print(ans)
# sq(7)