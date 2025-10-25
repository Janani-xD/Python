"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]

        def firstSearch(l, r):
            mid = (l + r) // 2
            while l < r:
                if nums[mid] > target:
                    l = mid + 1
                else:
                    r = mid
            return l if nums[l] == target else -1

        def lastSearch(l, r):
            mid = (l + r + 1) // 2
            while l < r:
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid
            return l if nums[l] == target else -1

        # first = firstSearch(0, len(nums) - 1)
        # print(first)
        last = lastSearch(0, len(nums) - 1)
        print(last)
        return [first, last]


obj1 = Solution()
# print(obj1.searchRange([], 8))
print(obj1.searchRange([5,7,7,8,8,10], 8))