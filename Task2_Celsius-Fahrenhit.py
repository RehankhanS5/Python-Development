def convert_temperature(value, unit):
    if unit.lower() == 'c':
        # Celsius to Fahrenheit
        return (value * 9/5) + 32, "Fahrenheit"
    elif unit.lower() == 'f':
        # Fahrenheit to Celsius
        return (value - 32) * 5/9, "Celsius"
    else:
        return None, None


# User input
temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

converted_value, converted_unit = convert_temperature(temperature, unit)

if converted_value is not None:
    print(f"Converted Temperature: {converted_value:.2f} {converted_unit}")
else:
    print("Invalid unit! Please enter C or F.")
