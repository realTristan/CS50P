# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: NUMB3RS                //
# //                                    //
# ////////////////////////////////////////

# // Main Function
def main():
    inp: str = input("IPv4 Address: ").strip()
    print(validate(inp))

# // Function to validate whether the provided
# // ip is valid or not
def validate(ip: str):
    try:
        # // Split the provided ip by it's '.'s
        split_ip: list[str] = ip.split(".")
        
        # // Check to make sure the ip has 4 sections
        if len(split_ip) < 4 or len(split_ip) > 4:
            return False
        
        # // Iterate over the split_ip array that
        # // Contains all the ip's sections
        for s in split_ip:
            if int(s) > 255:
                return False
            
    # // In Case of ValueError Exception, return false
    except ValueError:
        return False
    # // Else, valid ip, therefore return true
    return True

# // Run the main function
if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/numb3rs
# submit50 cs50/problems/2022/python/numb3rs