from typing import  List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return left + 1, right + 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

        # left, right = 0,len(numbers) - 1
        # while left < right:
        #     print(left, right)
        #     print(numbers[left],numbers[right])
        #     if numbers[left] + numbers[right] == target:
        #
        #         return left, right
        #         # return left + 1, right + 1
        #     left += 1
        #     right -= 1

my_obj = Solution()
print(my_obj.twoSum([2,7,11,15], 9))