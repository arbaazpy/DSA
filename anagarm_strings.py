def is_anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    
    list1 = list(string1)
    list2 = list(string2)

    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    
    return False

print(is_anagram("python", "typhon"), "should be anagram")
print(is_anagram("heart", "earth"), "should be anagram")
print(is_anagram("pure", "sure"), "should not be anagram")
print(is_anagram('abcde','edcba'), "should be anagram")