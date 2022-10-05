# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Coke Machine           //
# //                                    //
# ////////////////////////////////////////

# // Store the change owed
change_owed: int = 50

# // While the change owed is greater than 0
while change_owed > 0:
    print(f"Amount Due: {change_owed}")

    # // Get the inserted coin
    coin: int = int(input("Insert Coin: "))

    # // Make sure the coin is valid
    if coin in [50, 25, 10, 5]:
        change_owed -= coin

    # // Convert the negative to a positive
    if change_owed < 0:
        change_owed *= -1
        break

# // Print the change owed
print(f"Change Owed: {change_owed}")

# check50 cs50/problems/2022/python/coke
# submit50 cs50/problems/2022/python/coke