from typing import List

class Solution:
    def isValid(self, s): # Approach 1 using dictionary and stack
        mapping = {"{":"}","[":"]","(":")"}
        stack = []
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
        return not stack

my_obj = Solution()
print(my_obj.isValid("([])"))