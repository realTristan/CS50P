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
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# // Determine whether the plate is valid
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

main()

# check50 cs50/problems/2022/python/plates
# submit50 cs50/problems/2022/python/plates