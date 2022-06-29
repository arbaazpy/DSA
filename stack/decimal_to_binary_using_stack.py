from stack import Stack


def decimal_to_binary(decimal_number):
    """Converts a decimal number to a binary representation.

    Args:
        decimal_number (integer): integer decimal number eg., 255, 312, etc.

    Returns:
        string: binary string representation.
    """

    stack = Stack()
    start = True 

    while decimal_number > 0:
        remainder = decimal_number % 2
        stack.push(remainder)
        decimal_number = decimal_number // 2

    binary_string = ""
    while not stack.is_empty():
        binary_string += str(stack.pop())
    return binary_string

print(decimal_to_binary(233))
print(decimal_to_binary(42))
