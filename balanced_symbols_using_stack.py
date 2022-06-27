from stack import Stack


def balanced_symbols(symbols):
    """Checks if a string of symbols is balanced or not.
    Balanced symbols means that each opening symbol has a corresponding closing symbol and the pairs of symbols are properly nested.

    Args:
        symbols (str): string of symbols.

    Returns:
        bool: True if string is balanced else False.
    """

    stack = Stack()
    is_balanced = True
    index = 0

    while index < len(symbols) and is_balanced:
        if symbols[index] in ["(", "[", "{"]:
            stack.push(symbols[index])
        elif stack.is_empty():
            is_balanced = False
        elif (
            stack.peek() == "(" and symbols[index] == ")"
            or stack.peek() == "[" and symbols[index] == "]"
            or stack.peek() == "{" and symbols[index] == "}"
        ):
            stack.pop()
        else:
            is_balanced = False
        index += 1
        
    if stack.is_empty() and is_balanced:
        return True
    return False

print(balanced_symbols("((()))"))
print(balanced_symbols("(()"))

print("Balanced")
print(balanced_symbols("{{([][])}()}"))
print(balanced_symbols("[[{{(())}}]]"))
print(balanced_symbols("[][][](){}"))
print(balanced_symbols("[{}()[][]]"))

print()
print("Not balanced")
print(balanced_symbols("([)]"))
print(balanced_symbols("((()]))"))
print(balanced_symbols("[{()]"))
print(balanced_symbols("[{}()[)[]]"))
