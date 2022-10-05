# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Working 9 to 5         //
# //                                    //
# ////////////////////////////////////////
import re

# // Establish a regex for finding the work times
find_work_times = lambda x: re.findall(r"^\d.*\b(?= to)|(?<=to\s).*?[a-z]\b", x, re.IGNORECASE)
# // Establish a regex for checking if the provided
# // time has minutes in it
has_mins_regex = lambda x: re.match(r"^(1[0-2]|0?[1-9]):([0-5]?[0-9])$", x)
# // Establish a regex for checking if the provided
# // time has hours in it
has_hours_regex = lambda x: re.match(r"^(1[0-2]|0?[1-9])", x)

# // Main function
def main():
    hours: str = input("Hours: ").strip()
    print(convert(hours))


# // Function to handle the work_hours if the 
# // time has minutes in it
def handle_has_mins_AM(minutes: re.Match[str], work_hours: list[str]) -> list[str]:
    # // Establish group variables
    group_1: int = int(minutes.group(1))
    group_2: int = int(minutes.group(2))
    
    # // If invalid group
    if group_1 < 1 or group_1 > 12:
        raise ValueError
    
    # // Determine what string to append to the
    # // work_hours array
    elif group_1 == 12:
        return [*work_hours, f"00:{group_2}"]
    # // Time is greater than 9
    elif group_1 <= 9:
        return [*work_hours, f"0{group_1}:{group_2}"]
    # // Else, append default string
    return [*work_hours, f"{group_1}:{group_2}"]

# // Function to handle the work_hours if the 
# // time has hours in it
def handle_has_hours_AM(hours: re.Match[str], work_hours: list[str]) -> list[str]:
    group_1: int = int(hours.group(1))
    
    # // Determine what string to append to the
    # // work_hours array
    if group_1 == 12:
        return [*work_hours, f"00:00"]
    # // Time is greater than 9
    elif group_1 <= 9:
        return [*work_hours, f"0{group_1}:00"]
    # // Else, append default string
    return [*work_hours, f"{group_1}:00"]


# // Function to handle the work_hours if the 
# // time has minutes in it
def handle_has_mins_PM(minutes: re.Match[str], work_hours: list[str]) -> list[str]:
    # // Establish group variables
    group_1: int = int(minutes.group(1))
    group_2: int = int(minutes.group(2))
    
    # // If invalid group
    if group_1 > 12 or group_1 < 1:
        raise ValueError

    # // Determine what string to append to the
    # // work_hours array
    elif group_1 == 12:
        return [*work_hours, f"12:{group_2}"]
    return [*work_hours, f"{group_1 + 12}:{group_2}"]


# // Function to handle the work_hours if the 
# // time has hours in it
def handle_has_hours_PM(hours: re.Match[str], work_hours: list[str]) -> list[str]:
    group_1: int = int(hours.group(1))
    # // Determine what string to append to the
    # // work_hours array
    if int(group_1) == 12:
        return [*work_hours, f"12:00"]
    return [*work_hours, f"{group_1 + 12}:00"]


# // Function to handle the time if AM was used
def handle_AM(time: str, work_hours: list[str]) -> list[str]:
    # Check if the supplied times are 12 hour complex time.
    if minutes := has_mins_regex(time):
        return handle_has_mins_AM(minutes, work_hours)

    # Otherwise check if the supplied time is 12 hour simple time.
    elif hours := has_hours_regex(time):
        # // If invalid time, raise a ValueError
        if int(time) > 12 or int(time) < 1:
            raise ValueError
        # // Else, handle the time
        return handle_has_hours_AM(hours)
    raise ValueError

# // Function to handle the time if PM was used
def handle_PM(time: str, work_hours: list[str]) -> list[str]:
    # Check if the supplied times are 12 hour complex time.
    if minutes := has_mins_regex(time):
        return handle_has_mins_PM(minutes, work_hours)

    # Otherwise check if the supplied time is 12 hour simple time.
    elif hours := has_hours_regex(time):
        # // If invalid time, raise a ValueError
        if int(time) > 12 or int(time) < 1:
            raise ValueError
        # // Else, handle the time
        return handle_has_hours_PM(hours)
    raise ValueError


# // Function to covnert the inputted times
def convert(s: str) -> str:
    # // Establish work_hours list variable
    work_hours: list[str] = []
    # // Establish work_times list variable
    work_times: list = find_work_times(s)

    # Make sure there are only two time values supplied
    if len(work_times) > 2 or len(work_times) < 2:
        raise ValueError

    # // For each of the work times
    for time in work_times:
        time: str = str(time).lower()

        # // If the user inputted an AM time
        if " am" in time:
            time: str = time.strip(" am")
            work_hours = handle_AM(time, work_hours)

        # // If the user inputted a PM time
        elif " pm" in time:
            time: str = time.strip(" pm")
            work_hours = handle_PM(time, work_hours)

    # // Make sure there are two work hours
    if len(work_hours) == 2:
        return f"{work_hours[0]} to {work_hours[1]}"
    raise ValueError


# // Run the main function
if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/working
# submit50 cs50/problems/2022/python/working