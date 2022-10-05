
def main():
    s: str = input("Fraction: ")
    try:
        _split = s.split("/")
        x: int = int(_split[0])
        y: int = int(_split[1])
        if x > y or y == 0:
            raise Exception("Invalid x or y values")
        percent: int = int(round((x/y)*100))
        if percent <= 1:
            print("E")
        elif percent >= 99:
            print("F")
        else:
            print(f"{percent}%")
    except Exception:
        main()
main()

# check50 cs50/problems/2022/python/fuel
# submit50 cs50/problems/2022/python/fuel