# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Fuel Gauge             //
# //                                    //
# ////////////////////////////////////////

# // Main function
def main():
    inp: str = input("Input: ")
    print(shorten(inp))

# // Shorten the provided word function
def shorten(word: str):
    # // Iterate over the inputted string
    for i in range(len(word)):
        # // If character is a vowel
        if word[i].lower() in ["a", "e", "i", "o", "u"]:
            word = word[:i] + "u" + word[i+1:]

    # // Replace all 'u' from the string
    return word.replace("u", "")

# // Run the main function
if __name__ == "__main__":
    main()