from datetime import date, timedelta
import sys, inflect

# // Initialize the inflect engine
p = inflect.engine()


# // Main function
def main():
    # // Get the date of birth
    try:
        year, month, day = input("Date of Birth: ").split("-")
        year, month, day = int(year), int(month), int(day)
    except ValueError:
        sys.exit("Invalid Date")
    
    # // Convert the date to minutes
    print(convert_to_minutes(year, month, day))


# // Function to convert the date to minutes
def convert_to_minutes(year: int, month: int, day: int):
    # // Get the current date
    today: date = date.today()

    # // Calculate the difference between the two dates
    diff: timedelta = today - date(year, month, day)

    # // Convert the difference to minutes
    minutes: int = diff.days * 24 * 60

    # // Print the minutes
    return f"{p.number_to_words(minutes)} minutes".capitalize()


# // Run the main function
if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/seasons
# submit50 cs50/problems/2022/python/seasons