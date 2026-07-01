s = "abcabc"
count = 0
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        if "a" in s[i:j] and "b" in s[i:j] and "c" in s[i:j]:
            count += 1
print(count)


n = 5
for i in range(n):
    for j in range(n):
        print("*",end="")
    print("")

for i in range(n): #easy
    print("*"*n)

for i in range(1,n+1):
    print("*"*i)

for i in range(1, n+1):
    print(str(i)*i)

for i in range(1, n+1):
    if i == 1 or i == n:
        print("*"*n)
    else:
        print("*"," "*(n-2),"*", sep="")

for i in range(1, n+1):
    print(str(n-i+1)*(n-i+1))

for i in range(1, n+1):
    print(" "*(n-i),str(i)*i)