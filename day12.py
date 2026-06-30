# Number of Strings That Appear as Substrings in Word
pattern = ["a", "d", "c", "a"]
word = "abc"
count = 0

for el in pattern:
    n = word.count(el)
    if n != 0: # if el in word
        count += 1
print(count)

s = "abcabc"
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        print(s[i:j])