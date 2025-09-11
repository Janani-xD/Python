from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0, len(height) - 1
        max_area = 0
        while left < right:
            length = min(height[left], height[right])
            width = right - left
            area = length * width
            max_area = max(area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

my_obj = Solution()
print(my_obj.maxArea([1,8,6,2,5,4,8,3,7]))