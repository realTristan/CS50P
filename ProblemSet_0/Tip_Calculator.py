# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Tip Calculator         //
# //                                    //
# ////////////////////////////////////////
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    print(f"Leave ${(dollars * percent):.2f}")

# // Remove the '$' from the input
def dollars_to_float(d: str):
    return float(d.replace('$', ""))

# // Remove the '%' from the input
def percent_to_float(p: str):
    return float(p.replace('%', ""))/100

# // Run the main function
main()

# check50 cs50/problems/2022/python/tip
# submit50 cs50/problems/2022/python/tip