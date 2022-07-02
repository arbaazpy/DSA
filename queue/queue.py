
class Queue:
    """
    Create Queue abstract data type.
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Tests to see whether the queue is empty.
        It needs no parameters and returns a boolean value.

        Returns:
            bool: Returns true if queue is empty else false.
        """
        return self.items == []
    
    def enqueue(self, item):
        """Adds a new item to the rear of the queue.
        It needs the item and returns nothing. 0(n)

        Args:
            item (any): adds `item` on last place.
        """
        self.items.insert(0, item)
    
    def dequeue(self):
        """Removes the front item from the queue.
        It needs no parameters and returns the item.
        The queue is modified. 0(1)

        Returns:
            Any: Returns removed item.
        """
        return self.items.pop()

    def size(self):
        """Returns the number of items in the queue.
        It needs no parameters and returns an integer.

        Returns:
            int: size of the stack.
        """
        return len(self.items)

    def __str__(self):
        return f"{self.items}"


# q=Queue()
	
# q.enqueue(4)
# q.enqueue('dog')
# q.enqueue(True)
# print(q.size())
# print(q)
# print(q.dequeue())
# print(q)
