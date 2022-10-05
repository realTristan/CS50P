# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Adieu, Adieu           //
# //                                    //
# ////////////////////////////////////////
import sys, inflect

# // Define Variables
p = inflect.engine()
names: list[str] = []

# // Infinite loop till broken
while 1:
    try:
        # // Get the inputted name
        _names = input("Name: ").title()

        # // If invalid names, exit the program
        if len(_names) < 1:
            sys.exit(0)

        # // Append the new names to the
        # // global names array
        names.append(_names)

    # // Except Control+D was pressed
    except EOFError:
        print(f"\nAdieu, adieu, to {p.join(names)}")
        break

# check50 cs50/problems/2022/python/adieu
# submit50 cs50/problems/2022/python/adieu