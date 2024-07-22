# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Felipe's Taqueria      //
# //                                    //
# ////////////////////////////////////////
def main():
    is_available()

def is_availabe():
    MENU= {
        "baja taco": 4.00,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 8.50,
        "super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00
    }
    
    # // Store the total cost
    total: int = 0
    
    while 1:
        try:
            # // Get the item
            item= input("Item: ").lower()
    
            # // Increase the total by the value
            # // from the item in the MENU map
            if item in MENU:
                total += MENU[item]
    
            # // Print the new total formatted to 2 decimal points
                print(f"Total: ${total:.2f}")
            elif item=='burger':
                is_available()
            else:
                exit()
                
    
        # // Except Control+D is pressed
        except EOFError:
            break

main()

# https://github.com/settings/tokens
# check50 cs50/problems/2022/python/taqueria
# submit50 cs50/problems/2022/python/taqueria
