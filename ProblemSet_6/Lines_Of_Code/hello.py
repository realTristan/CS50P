# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Lines of Code Test     //
# //                                    //
# ////////////////////////////////////////

# Another Test Program
def main():
    name: str = input("whats your name? ")
    print(hello(name))


# There should only be an output of 5 lines
def hello(to: str) -> str:
    return f"hello, {to}"



