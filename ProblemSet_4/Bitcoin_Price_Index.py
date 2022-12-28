# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Bitcoin Price Index    //
# //                                    //
# ////////////////////////////////////////
import requests, sys

# // Check Command-Line Arguments
def check_args():
    # // If not enough arguments
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")

    # // If the argument isn't a number
    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")

try:
    # // Check CL Args
    check_args()

    # // Send an http request to the coindesk api
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    # // Get the rate from the response json and
    # // establish a 'per_coin' value
    rate: int = r.json()["bpi"]["USD"]['rate_float']
    per_coin = rate * float(sys.argv[1])

    # // Print the result
    print(f"${per_coin:,.4f}")

except requests.RequestException:
    sys.exit()

# check50 cs50/problems/2022/python/bitcoin
# submit50 cs50/problems/2022/python/bitcoin