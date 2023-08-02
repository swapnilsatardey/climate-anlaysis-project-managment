import sys
import temperature_conversion
import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

script = sys.argv[0]
assert len(sys.argv) == 2, script + ": requires filename"
filename = sys.argv[1]

climate_data = open(filename, 'r')

for line in climate_data:
    data = line.split(',')

    # Don't process comment lines, which start with '#'
    if data[0][0] == '#':
        pass
    # Extract our max temperature in Fahrenheit - 4th column
    # Don't process invalid temperature readings of -9999
    else:
        fahr = float(data[3])
        if fahr != -9999:
            celsius = temperature_conversion.convert_fahrenheit_to_celsius(fahr)
            kelvin = temperature_conversion.convert_fahrenheit_to_kelvin(fahr)
            print(str(celsius)+", " + str(kelvin))
