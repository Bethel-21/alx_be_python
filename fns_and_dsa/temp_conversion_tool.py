

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5



take_input = int(input("Enter the temperature to convert: "))
another_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")


def convert_to_celsius():
    return (take_input - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit():
    return (take_input * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if another_input == "C":
    print(f"{take_input}.0°C is {convert_to_fahrenheit()}.0°F")
elif another_input == "F":
    print(f"{take_input}.0°F is {convert_to_celsius()}.0°C")
else:
    print("Invalid temperature.Please enter a numberic value")