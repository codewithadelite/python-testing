from ..temperature import celsius_to_fahrenheit

def test_can_convert_celcius_to_fahrenheite():
    try:
        assert celsius_to_fahrenheit(0) == 32
        print("OK")
    except AssertionError:
        print("FAIL")

    try:
        assert celsius_to_fahrenheit(100) == 212
        print("OK")
    except AssertionError:
        print("FAIL")