# ////////////////////////////////////////////
# //                                        //
# // Name: Tristan Simpson                  //
# //                                        //
# // Assignment: Just setting up my twittr  //
# //                                        //
# ////////////////////////////////////////////

# // Get the user input
s: str = input("Input: ")

# // Iterate over the inputted string
for i in range(len(s)):
    # // If chatacter is a vowel
    if s[i].lower() in ["a", "e", "i", "o", "u"]:
        s = s[:i] + "u" + s[i+1:]

# // Replace all 'u' from the string
s = s.replace("u", "")
print(s)

# check50 cs50/problems/2022/python/twttr
# submit50 cs50/problems/2022/python/twttr