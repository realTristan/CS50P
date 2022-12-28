# ////////////////////////////////////////////////
# //                                            //
# // Name: Tristan Simpson                      //
# //                                            //
# // Assignment: Regular, um, Expressions       //
# //                                            //
# ////////////////////////////////////////////////
import re

# // Main function
def main():
    inp: str = input("Text: ")
    print(count(inp))

# // Function to check how many times "um" appears
# // in the provided string
def count(s: str):
    res: list[str] = re.findall(r"^um\b|(?<=\s)um\b", s, re.IGNORECASE)
    return len(res)

# // Run the main function
if __name__ == "__main__":
    main()
    
# check50 cs50/problems/2022/python/um
# submit50 cs50/problems/2022/python/um