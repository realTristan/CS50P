
s: str = input("Input: ")
for i in range(len(s)):
    try:
        if s[i].lower() in ["a", "e", "i", "o", "u"]:
            s = s[:i] + s[i+1:]
    except Exception: break

print(f"Output: {s}")

# check50 cs50/problems/2022/python/twttr
# submit50 cs50/problems/2022/python/twttr