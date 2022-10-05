# ////////////////////////////////////////////
# //                                        //
# // Name: Tristan Simpson                  //
# //                                        //
# // Assignment: Home Federal Savings Bank  //
# //                                        //
# ////////////////////////////////////////////

# // Get the user input
s: str = input("Greeting: ")
s = s.lower().strip()

# // Check what the input startswith
if s.startswith("hello"):
    print("$0")
elif s.startswith("h"):
    print("$20")
else:
    print("$100")

# check50 cs50/problems/2022/python/bank
# submit50 cs50/problems/2022/python/bank