
def division(a, b):
    # if a or b is not a number, raise a ValueError
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Invalid input")
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b
