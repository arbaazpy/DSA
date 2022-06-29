from stack import Stack


def balanced_parentheses(parentheses):
    """Checks if a string parentheses is balanced or not.
    Balanced parentheses means that each opening symbol has a corresponding closing symbol and the pairs of parentheses are properly nested.

    Args:
        parentheses (str): string of parentheses.

    Returns:
        bool: True if string is balanced else False.
    """

    stack = Stack()
    is_balanced = True
    index = 0

    while index < len(parentheses) and is_balanced:
        if parentheses[index] == "(":
            stack.push(parentheses[index])
        elif stack.is_empty():
            is_balanced = False
        else:
            stack.pop()
        index += 1
        
    if stack.is_empty() and is_balanced:
        return True
    return False

print(balanced_parentheses('((()))'))
print(balanced_parentheses('(()'))

print("Balanced")
print(balanced_parentheses('(()()()())'))
print(balanced_parentheses('(((())))'))
print(balanced_parentheses('(()((())()))'))

print()
print("Not balanced")
print(balanced_parentheses('((((((())'))
print(balanced_parentheses('()))'))
print(balanced_parentheses('(()()(()'))
