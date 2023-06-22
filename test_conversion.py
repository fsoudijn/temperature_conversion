from conversion import celsius_to_fahrenheit
from conversion import kelvin_to_fahrenheit
import pytest

def test_celsius_to_fahrenheit():
    fahr = celsius_to_fahrenheit(20)
    tiny_fahr = 1e06
    assert fahr == 68
    assert celsius_to_fahrenheit(30) == 86
    assert celsius_to_fahrenheit(0) == 32

def test_kelvin_to_fahrenheit():
    tiny_kelvin = 1e06
    assert kelvin_to_fahrenheit(40) == pytest.approx(387.67,tiny_kelvin)

def test_celsius_to_fahrenheit_invalid():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("Invalid")

def test_celsius_to_fahrenheit_none():
    assert celsius_to_fahrenheit(None) is None


def test_that_doesnot_do_anything():
    celsius_to_fahrenheit(0)