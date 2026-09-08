def add(x,y):
    print("adding two numbers:",x,y)
    return x + y

def sub(x,y):
    print("subracting two numbers:",x,y)
    return x - y

def mul(x,y):
    print("multiplying two numbers:",x,y)
    return x * y

def divide(x, y):
    """Divide two numbers with zero-division check."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        return x / y