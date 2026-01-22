def area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Lungimea si latimea trebuie sa fie pozitive.")
    return length * width

def perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Lungimea si latimea trebuie sa fie pozitive.")
    return 2 * (length + width)
