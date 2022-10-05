
s: str = input("Greeting: ")
s = s.lower().strip()

if s.startswith("hello"):
    print("$0")
elif s.startswith("h"):
    print("$20")
else:
    print("$100")

# check50 cs50/problems/2022/python/bank
# submit50 cs50/problems/2022/python/bank