# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Fuel Gauge             //
# //                                    //
# ////////////////////////////////////////

# // Main function
def main():
    # // Get the fraction the convert to a 
    # // Percentage integer
    fraction: str = input("Fraction: ")
    percentage: int = convert(fraction)

    # // Print the gauge percentage
    print(gauge(percentage))

# // Convert the fraction to an integer
def convert(fraction: str):
    try:
        # // Split the inputted fraction by "/"
        _split = fraction.split("/")
        
        # // Get the x and y values
        x: int = int(_split[0])
        y: int = int(_split[1])

        # // Return the percentage integer
        return int(round((x/y)*100))

    # // Except Exceptions, ValueError and ZeroDivisionError
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError

# // Convert the percentage integer to a
# // percentage string, E or F
def gauge(percentage):
    # // If fuel gauge is empty
    if percentage <= 1:
        return "E"

    # // Else if fuel gauge is full
    elif percentage >= 99:
        return "F"
    
    # // Else, return the percentage
    return f"{percentage}%"

# // Run the main function
if __name__ == "__main__":
    main()