
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        left , right = 0 , len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    def isPalindrome_faster(self, s):
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        return s == s[::-1]

    def isPalindrome_fastest(self, s):
        lower = s.lower()
        chars = ''.join([char for char in lower if char.isalnum()])
        return chars == chars[::-1]

my_obj = Solution()
print(my_obj.isPalindrome("A man, a plan, a canal: Panama"))
print(my_obj.isPalindrome_faster("A man, a plan, a canal: Panama"))