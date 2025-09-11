from typing import  List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        print(left, right)
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

my_obj = Solution()
print(my_obj.reverseString(["h","e","l","l","o"]))