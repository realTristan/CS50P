# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Vanity Plates Test     //
# //                                    //
# ////////////////////////////////////////
from plates import is_valid

# // Testing the is_valid function
assert is_valid("CS50")
assert not is_valid("H")
assert not is_valid("AI2.14")
assert not is_valid("thistoolong")
assert not is_valid("AAA22A")
assert not is_valid("CS05")
assert not is_valid("57EED")
assert not is_valid("32")