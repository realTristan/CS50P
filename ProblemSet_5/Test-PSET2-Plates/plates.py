# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Vanity Plates          //
# //                                    //
# ////////////////////////////////////////

# // Main function
def main():
    plate: str = input("Plate: ")
    return is_valid(plate)

# // Function to check if plate is valid
def is_valid(s: str):
    # // If length is invalid
    if len(s) < 2 or len(s) > 6:
        return False

    # // If the first two characters are not a letter
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # // Store whether number has been found
    foundNum: bool = False
    firstNum: bool = True

    # // For each character in the string
    for c in s:
        # // Check if the current character is a digit
        if c.isdigit():
            foundNum = True
            # // Check if first num
            if firstNum:
                # // first num is a 0
                if c == "0":
                    return False
                firstNum = False
        
        # // If letter comes after the number, return false
        elif c.isalpha():
            if foundNum:
                return False
        else:
            return False
    return True

# // Run the main function
if __name__ == "__main__":
    main()