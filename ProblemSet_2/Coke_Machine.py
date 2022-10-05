
change_owed: int = 50
while change_owed > 0:
    print(f"Amount Due: {change_owed}")
    coin: int = int(input("Insert Coin: "))
    if coin in [50, 25, 10, 5]:
        change_owed-=coin
    if change_owed < 0:
        change_owed *= -1
        break

print(f"Change Owed: {change_owed}")

# check50 cs50/problems/2022/python/coke
# submit50 cs50/problems/2022/python/coke