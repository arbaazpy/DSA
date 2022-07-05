"""
- Given a string s of lower and upper case English letters.
- A good string is a string which doesn’t have two adjacent characters s[i] and s[i + 1] where: 0 <= i <= s.length-2
- s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
- To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.
- Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
- Notice that an empty string is also good.
- https://leetcode.com/problems/make-the-string-great/

Example 1:
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
"""

from stack import Stack


def make_good(string: str) -> str:
    """Removes bad characters from a string.
    string[i] is a lower-case letter and string[i + 1] is the same letter but in upper-case or vice-versa.
    To make the string good, you can choose two adjacent characters that make the string bad and remove them.
    You can keep doing this until the string becomes good.
    Args:
        string (str): input string.

    Returns:
        str: a good string.
    """
    stack = Stack()
    for charcter in string:
        if not stack.is_empty() and charcter.lower() == stack.peek().lower() and charcter != stack.peek():
            stack.pop()
        else:
            stack.push(charcter)
    return "".join(stack.items)

print(make_good("leEeetcode"))
print(make_good("abBAcC"))
print(make_good("s"))
