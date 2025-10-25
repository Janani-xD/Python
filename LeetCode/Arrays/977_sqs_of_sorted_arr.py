"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        beg , end = 0, len(nums) - 1
        index = len(nums) - 1
        while index >= 0:
            if abs(nums[p2]) > abs(nums[p1]):
                output[index] = nums[p2] * nums[p2]
                p2 -= 1
            else:
                output[index] = nums[p1] * nums[p1]
                p1 += 1
            index -= 1
        return output
        # return sorted([x**2 for x in nums])

