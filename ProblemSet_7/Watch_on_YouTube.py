# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Watch on Youtube       //
# //                                    //
# ////////////////////////////////////////
import re

# // Main function
def main():
    html: str = input("HTML: ").strip()
    print(parse(html))

# // Function to extract the embed url
def parse(s: str):
    try:
        # // Use re to extract
        url: re.Match[str] = re.search('(?<=embed\/).*?(?=")', s)
        # // Return the extracted embed
        return f"https://youtu.be/{url.group(0)}"
    except Exception:
        return None

# // Run the main function
if __name__ == "__main__":
    main()
    
# check50 cs50/problems/2022/python/watch
# submit50 cs50/problems/2022/python/watch