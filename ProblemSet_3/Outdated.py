# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Outdated               //
# //                                    //
# ////////////////////////////////////////

# // An array of MONTHS for converting a month name
# // to the month's numeral
MONTHS: list[str] = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# // Function to get the month numeral. Using
# // a function is better because it can just
# // return if the month is found instead of
# // having to finish iterating the array
def get_month_numeral(_m: str) -> int:
    # // Iterate over the MONTHS
    for i in range(len(MONTHS)):
        if _m == MONTHS[i]:
            return i + 1

# // Function to check if the provided month
# // and day are valid
def is_valid_date(m: int, d: int) -> bool:
    return (int(m) > 0 and int(m) < 13) and (int(d) > 0 and int(d) < 32)

# // Infinite loop for getting the date until broken
while True:
    date: str = input("Date: ").strip()
    try:
        # // Split the date by slashes
        m, d, y = date.split("/")

        # // Break if valid date
        if is_valid_date(m, d): break

    except Exception:
        try:
            # // Split the date by spaces and remove comma
            _m, _d, y = date.split(" ")

            # // Make sure date is valid
            if "," in date:
                d: str = _d.replace(",", "")

                # // Iterate over the MONTHS
                m: int = get_month_numeral(_m)

                # // Break if valid date
                if is_valid_date(m, d): break
        except Exception:
            pass

# // Print the result
print(f"{y}-{int(m):02}-{int(d):02}")

# check50 cs50/problems/2022/python/outdated
# submit50 cs50/problems/2022/python/outdated