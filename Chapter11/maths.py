class Maths:
    """Math operations"""

    def __init__(self, decimals = 2):
        self.decimals = decimals

    def division(self, a, b):
        """Divide two numbers"""
        # if a or b is not a number, raise a ValueError
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Invalid input")
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        # show only the decimals specified
        return round(a / b, self.decimals)
