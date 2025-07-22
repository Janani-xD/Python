from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        pointer = 0
        res_str = ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        while pointer >= 0 and pointer < len(first):
            if first[pointer] == last[pointer]:
                res_str += first[pointer]
                pointer += 1
            else:
                return res_str
        return res_str


common_obj = Solution()
print(common_obj.longestCommonPrefix(["flow", "flight", "flower"]))