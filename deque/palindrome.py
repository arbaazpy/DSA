from deque import Deque


def check_palindrome(string: str) -> bool:
    """Checks whether the given string is a palindrome or not.

    Args:
        string (str): input string

    Returns:
        bool: True if string is a palindrome else False.
    """
    deque = Deque()
    is_palindrome = True
    
    for character in string:
        deque.add_front(character)
    
    while deque.size() > 1 and is_palindrome:
        front_character = deque.remove_front()
        rear_character = deque.remove_rear()
        if front_character != rear_character:
            is_palindrome = False

    return is_palindrome

print(check_palindrome("radar"))
print(check_palindrome("pussy"))
