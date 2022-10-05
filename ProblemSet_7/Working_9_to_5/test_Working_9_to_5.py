from Working_9_to_5 import convert
import pytest

# // Test the convert function
def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 PM to 12:00 PM") == "12:00 to 12:00"
    
    # // Test for Value Errors
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
        convert(" to ")
        convert("14:00 AM to 13:00 PM")
        convert("0:00 AM to 0:00 PM")
        convert("13 AM to 15 PM")
        convert("0 AM to 0 PM")
        convert("13:67 AM to 7:61 PM")
        convert("9AM to 5PM")
        convert("6:19 AM 4:20 PM")