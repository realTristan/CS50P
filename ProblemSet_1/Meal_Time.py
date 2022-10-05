# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Meal Time              //
# //                                    //
# ////////////////////////////////////////

# // Main function
def main():
    time: str = input("What time is it? ")
    time_as_num: float = convert(time)

    # // Determine what time it is
    if time_as_num >= 700 and time_as_num <= 800:
        print("breakfast time")
    elif time_as_num >= 1200 and time_as_num <= 1300:
        print("lunch time")
    elif time_as_num >= 1800 and time_as_num <= 1900:
        print("dinner time")

# // Convert the input to a float time
def convert(time: str):
    return float(time.replace(":", ""))

# // Run the main function
if __name__ == "__main__":
    main()
    
# check50 cs50/problems/2022/python/meal
# submit50 cs50/problems/2022/python/meal