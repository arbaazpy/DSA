from stack import Stack


def reverse_string(string):
    stack = Stack()
    for character in string:
        stack.push(character)
    return "".join(stack.pop() for _ in range(stack.size()))
        
    
print(reverse_string('apple'))
print(reverse_string('x'))
print(reverse_string('1234567890'))