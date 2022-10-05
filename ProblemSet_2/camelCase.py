# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: camelCase              //
# //                                    //
# ////////////////////////////////////////

# // Get the camelCase input
s: str = input("camelCase: ")

# // Iterate over the characters in the camelCase input
for i in range(len(s)):
    # // Convert the uppercase to a _(character)
    if s[i].isupper():
        s = s[:i] + "_"+s[i].lower() + s[i+1:]

# // Print the formatted snake_case
print(f"snake_case: {s}")

# check50 cs50/problems/2022/python/camel
# submit50 cs50/problems/2022/python/camel