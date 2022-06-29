# Create a stack

class Stack:
    """
    Create Stack data type.
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Checks for empty stack.

        Returns:
            bool: Returns true if stack is empty else false.
        """
        return self.items == []
    
    def push(self, item):
        """Add an item to the stack.

        Args:
            item (any): adds `item` on last place.
        """
        self.items.append(item)
    
    def pop(self):
        """Removes last item from the stack.

        Returns:
            Any: Returns removed item.
        """
        return self.items.pop()

    def peek(self):
        """Get top (last) item from the stack.

        Returns:
            Any: Returns latest item added to the stack.
        """
        return self.items[-1]
    
    def size(self):
        """Returns the size of the stack.

        Returns:
            int: size of the stack.
        """
        return len(self.items)

    def __str__(self):
        return f"{self.items}"

# stack = Stack()

# print()
# print("is empty", stack.is_empty())
# stack.push(4)
# stack.push("dog")
# print()
# print("peek", stack.peek())
# stack.push(True)
# print("size", stack.size())
# print("is empty", stack.is_empty())
# stack.push(8.4)
# print("pop", stack.pop())
# print("pop", stack.pop())
# print("size", stack.size())

# print()
# print("stack items", stack)
