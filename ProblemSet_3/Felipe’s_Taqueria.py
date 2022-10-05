menu: dict[str, float] = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "bachos": 11.00,
    "quesadilla": 8.50,
    "super Burrito": 8.50,
    "super Quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}
total: int = 0
while 1:
    try:
        item: str = input("Item: ")
        if item in menu:
            total += menu[item]
            print(f"Item: ${menu[item]}")
        print(f"Total: ${total:.2f}")
    except EOFError:
        break

# check50 cs50/problems/2022/python/taqueria
# submit50 cs50/problems/2022/python/taqueria