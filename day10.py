l1 = [2, 4, 3]
l2 = [5, 6, 4]

num1 = 0
num2 = 0

l1.reverse()
l2.reverse()

for el in l1:
    num1 = num1 * 10 + el
for el2 in l2:
    num2 = num2 * 10 + el2

result = num1 +num2
l3 = []
while result > 0:
    l3.append(result % 10)
    result = result // 10

print(l3)