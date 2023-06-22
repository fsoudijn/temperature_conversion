def celsius_to_fahrenheit(celsius):
    """ Celsius to Fahrenheit conversion

    Args:
        celsius (float): temperature in degrees celsius

    Returns:
        float: temperature in degrees fahrenheit
    """
    if celsius is None: 
        return(None)
    return celsius/5*9 + 32

def fahrenheit_to_celsius(fahrenheit):
    if fahrenheit is None: 
        return(None)
    return (fahrenheit - 32) * (5 / 9)

def celsius_to_kelvin(celsius):
    """ Celsius to Kelvin conversion

    Args:
        celsius (float): temperature in degrees celsius

    Returns:
        float: temperature in degrees kelvin
    """
    if celsius is None: 
        return(None)
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    if kelvin is None: 
        return(None)
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    """ Kelvin to Fahrenheit conversion

    Args:
        kelvin (float): temperature in degrees kelvin

    Returns:
        float: temperature in degrees fahrenheit
    """
    if kelvin is None: 
        return(None)
    celsius = kelvin - 273.15
    return celsius_to_fahrenheit(celsius)

def check_temperature_validity(temperature, unit):
    abs_zero = {"C": -273.15,
                "F": -459.67,
                "K": 0}
    if temperature < abs_zero[unit]:
        return False
    return True

def check_unit_validity(unit):
    if not unit in ["C", "F", "K"]:
        return False
    return True