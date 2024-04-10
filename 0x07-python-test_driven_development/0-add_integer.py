def add_integer(a, b=98):
    # Check if a is an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    
    # Check if b is an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    
    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)
    
    # Perform the addition of a and b
    result = a + b
    
    return result
