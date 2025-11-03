# temp_conversion_tool.py

# ✅ Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    # Use the global variable
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    # Use the global variable
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """Main function to interact with the user."""
    try:
        # Prompt the user to enter temperature
        temperature_input = input("Enter the temperature to convert: ")
        temperature = float(temperature_input)  # Validate numeric input
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Ask for the unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
        # Convert Celsius to Fahrenheit
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
    elif unit == 'F':
        # Convert Fahrenheit to Celsius
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()

