# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Fuel Gauge             //
# //                                    //
# ////////////////////////////////////////

# // Main function
def main():
    s: str = input("Fraction: ")
    try:
        # // Split the inputted fraction by "/"
        _split = s.split("/")
        x: int = int(_split[0])
        y: int = int(_split[1])
        
        # // If x or y is invalid
        if x > y or y == 0:
            raise Exception("Invalid x or y values")

        # // Convert the percent from a decimal
        percent: int = int(round((x/y)*100))

        # // If fuel gauge is empty
        if percent <= 1:
            print("E")

        # // Else if fuel gauge is full
        elif percent >= 99:
            print("F")
        
        # // Else, print the fuel percent
        else:
            print(f"{percent}%")

    # // Function Recursion
    except Exception:
        main()

# // Run the main function
main()

# check50 cs50/problems/2022/python/fuel
# submit50 cs50/problems/2022/python/fuel