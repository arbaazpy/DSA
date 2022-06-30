from stack import Stack


def base_converter(decimal_number:int, base:int) -> str:
    """Converts a decimal number to given base representation.

    Args:
        decimal_number (integer): integer decimal number eg., 255, 312, etc.

    Returns:
        string: expected base representation.
    """

    stack = Stack()
    start = True 

    while decimal_number > 0:
        remainder = decimal_number % base
        stack.push(remainder)
        decimal_number //= base

    binary_string = ""
    while not stack.is_empty():
        top = str(stack.pop())
        hexadecimal_number = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}
        if top in hexadecimal_number:
            top = hexadecimal_number[top]
        binary_string += top
    return binary_string

print(base_converter(25, 2))
print(base_converter(25, 16))
print(base_converter(25, 8))
print(base_converter(256, 16))
print(base_converter(26, 26))

print(base_converter(300, 16))
print(base_converter(242, 16))
print(base_converter(81, 16))
