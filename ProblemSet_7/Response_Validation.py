# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Response Validation    //
# //                                    //
# ////////////////////////////////////////
import validators

# // Main function
def main():
    print(validate(input("What's your email address? ").strip()))

# // Function to return whether the email address is valid
def validate(address: str):
    return "Valid" if validators.email(address) else "Invalid"

# // Run the main function
if __name__ == "__main__":
    main()
    
# check50 cs50/problems/2022/python/response
# submit50 cs50/problems/2022/python/response