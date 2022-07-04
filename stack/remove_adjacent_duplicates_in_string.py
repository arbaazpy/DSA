"""
Remove All Adjacent Duplicates In String, by Facebook, Amazon, Bloomberg, Oracle
- Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
- We repeatedly make duplicate removals on S until we no longer can.
- Return the final string after all such duplicate removals have been made. It is guaranteed the answer is unique.

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.
he result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
"""

from stack import Stack


def remove_duplicates(string: str) -> str:
    """Removes duplicate characters for a given string.

    Args:
        string (str): input string

    Returns:
        str: string which has no duplicate characters.
    """
    stack = Stack()
    for character in string:
        if not stack.is_empty() and stack.peek() == character:
            stack.pop()
        else:
            stack.push(character)
    return "".join(stack.items)

print(remove_duplicates("azxxzy"))
print(remove_duplicates("abbaca"))
