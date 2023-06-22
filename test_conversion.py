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