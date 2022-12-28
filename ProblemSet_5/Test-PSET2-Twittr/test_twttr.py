# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Twttr Test             //
# //                                    //
# ////////////////////////////////////////
from twttr import shorten

# // Test the shorten function
def test_shorten():
    assert shorten("testing") == "tstng"
    assert shorten("this is my tweet!") == "ths s my twt!"
    assert shorten("UPPERCASE") == "PPRCS"
    assert shorten("s0meth1ng") == "s0mth1ng"

# check50 cs50/problems/2022/python/tests/twttr
# check50 cs50/problems/2022/python/tests/twttr