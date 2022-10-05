
s: str = input("camelCase: ")

for i in range(len(s)):
    if s[i].isupper():
        s = s[:i] + "_"+s[i].lower() + s[i+1:]
print(f"snake_case: {s}")

# check50 cs50/problems/2022/python/camel
# submit50 cs50/problems/2022/python/camel