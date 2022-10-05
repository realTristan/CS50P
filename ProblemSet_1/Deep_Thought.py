# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Deep Thought           //
# //                                    //
# ////////////////////////////////////////

# // Store valid 'Yes' inputs
yes_list: list[str] = ["forty-two", "42", "forty two"]

# // Get the user input
s: str = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

# // Check if the input is in the yes_list
if s.lower().strip() in yes_list:
    print("Yes")
else:
    print("No")

# check50 cs50/problems/2022/python/deep
# submit50 cs50/problems/2022/python/deep