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


s = Stack()
print()
print("is empty", s.is_empty())
s.push(4)
s.push("dog")
print()
print("peek", s.peek())
s.push(True)
print("size", s.size())
print("is empty", s.is_empty())
s.push(8.4)
print("pop", s.pop())
print("pop", s.pop())
print("size", s.size())