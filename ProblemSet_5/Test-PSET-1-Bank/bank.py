# ////////////////////////////////////////////
# //                                        //
# // Name: Tristan Simpson                  //
# //                                        //
# // Assignment: Home Federal Savings Bank  //
# //                                        //
# ////////////////////////////////////////////

# // Get the user input
def main():
    s: str = input("Greeting: ")
    s = s.lower().strip()
    print(value(s))

# // Handle the greeting
def value(greeting: str):
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

# // Run the main function
if __name__ == "__main__":
    main()