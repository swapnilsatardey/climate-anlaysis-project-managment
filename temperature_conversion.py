"""
Converter for temperature scales
"""

def convert_fahrenheit_to_celsius(f):
    c = (f - 32) * (5 / 9)
    return c

def convert_fahrenheit_to_kelvin(f):
    c = convert_fahrenheit_to_celsius(f)
    k = c + 273.15
    return k
