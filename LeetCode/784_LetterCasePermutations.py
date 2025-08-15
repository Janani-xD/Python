from typing import  List
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [] #
        left = len(s) -1
        while left >=0:
            if s[left].isalpha():
                
                res.append()


my_obj = Solution()
print(my_obj.letterCasePermutation("a1b2"))



# char_count = sum(1 for char in s if char.isalpha())
# print(char_count)
# res = [''] * pow(2, char_count)
# print(res)
# for elem in s:
#     if elem.isdigit():
#         for str in res:
#             str += elem
#     else:
#         for i in range(char_count):
#             res[i] = res[i] + elem.lower()
#         for i in range(char_count + 1, len(res)):
#             res[i] = res[i] + elem.upper()
# return res
