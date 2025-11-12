class Calculator:
    """
    A simple calculator demonstrating class methods and static methods.
    """

    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        Does not depend on class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        Accesses the class attribute 'calculation_type'.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
