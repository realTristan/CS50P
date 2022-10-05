
s: str = input("Input: ")
for i in range(len(s)):
    if s[i].lower() in ["a", "e", "i", "o", "u"]:
        s = s[:i] + "u" + s[i+1:]

s = s.replace("u", "")
print(s)

# check50 cs50/problems/2022/python/twttr
# submit50 cs50/problems/2022/python/twttr