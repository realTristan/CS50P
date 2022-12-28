# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Bank Test              //
# //                                    //
# ////////////////////////////////////////
from bank import value

# // Test the value function
def test_value():
    assert value("Hello") == 0
    assert value("How are you doing?") == 20
    assert value("What's happening?") == 100

# check50 cs50/problems/2022/python/tests/bank
# check50 cs50/problems/2022/python/tests/bank