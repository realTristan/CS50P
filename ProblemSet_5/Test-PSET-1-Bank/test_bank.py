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