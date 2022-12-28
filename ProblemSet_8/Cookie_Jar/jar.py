class Jar:
    # capacity non negative, otherwise valueerror
    def __init__(self, capacity: int = 12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    # // Return a string representation of the jar, using 🍪 to represent each cookie in the jar.
    def __str__(self):
        return "🍪" * self.size

    # // Add cookies to the jar. If there are too many cookies to fit in the jar, raise a ValueError.
    def deposit(self, amount: int):
        if amount > self.capacity or amount + self.size > self.capacity:
            raise ValueError
        self._size += amount

    # // Remove cookies from the jar. If there are not enough cookies in the jar, raise a ValueError.
    def withdraw(self, amount: int):
        if amount > self.size:
            raise ValueError
        self._size -= amount

    # // The capacity property returns the maximum number of cookies the jar can hold.
    @property
    def capacity(self):
        return self._capacity 

    # // The size property returns the number of cookies in the jar.
    @property
    def size(self):
        return self._size

# // Testing the jar class
def main():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    print(jar.capacity)
    print(jar.size)

if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/jar
# submit50 cs50/problems/2022/python/jar