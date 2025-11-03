# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Perform division safely with error handling.

    Parameters:
    numerator (str or float): The numerator value.
    denominator (str or float): The denominator value.

    Returns:
    str: The result of division or an error message.
    """
    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        # Attempt division
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
