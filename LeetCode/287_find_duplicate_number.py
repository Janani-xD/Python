
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # using cycle detection in linked list
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow



my_obj = Solution()
print(my_obj.findDuplicate([1,4,4,2,0]))