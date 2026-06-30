s = "abc"
count = 0
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        if "a" in s[i:j] and "b" in s[i:j] and "c" in s[i:j]:
            count += 1
print(count)