import pytest
from jar import Jar

# // Test the initialization of the Jar class
def test_init():
    Jar()


# // Test the constructor
def test_str():
    # // Initialize the jar
    jar = Jar()

    # // Test the jar functions
    assert str(jar) == ""
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪"
    jar.deposit(8)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


# // Test the deposit function and size property
def test_deposit():
    # // Initialize the jar
    jar = Jar()

    # // Test the jar functions
    jar.deposit(6)
    assert jar.size == 6
    with pytest.raises(ValueError):
        jar.deposit(89)


# // Test the withdraw function
def test_withdraw():
    # // Initialize the jar
    jar = Jar()

    # // Test the jar functions
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(64)
