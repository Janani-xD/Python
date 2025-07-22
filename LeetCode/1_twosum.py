""""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

I/P : nums = [2,7,11,15], target = 9 Output : [0,1]
I/P : nums = [3,2,4], target = 6 Output : [1,2]
I/P : nums = [3,3], target = 6 Output : [0,1]

"""

# Approach 1:
# Approach 2:

from typing import List
import copy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Using sorting and pointers
        nums1 = copy.deepcopy(nums)
        nums1.sort()
        left = len(nums) - 1
        right = 0
        while True:
            right_obj = nums1[right]
            left_obj = nums1[left]
            sum = right_obj + left_obj
            if sum == target:
                return [nums.index(right_obj), nums.index(left_obj)]
            elif sum > target:
                left -= 1
            else:
                right += 1

        # # Using Dict
        # dict_set = {}
        # for index, element in enumerate(nums):
        #     print(dict_set,element)
        #     difference = target - element
        #     if difference not in dict_set:
        #         dict_set[element] = index
        #     else:
        #         return [dict_set[difference], index]

obj = Solution()
print(obj.twoSum([2,7,11,15],9))