from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        class Solution:
            def threeSum(self, nums: List[int]) -> List[List[int]]:
                nums.sort()
                ans = []
                for index, num in enumerate(nums):
                    if nums[index] > 0:
                        break
                    elif index > 0 and nums[index] == nums[index - 1]:
                        continue
                    left = index + 1
                    right = len(nums) - 1

                    while left < right:
                        sum = num + nums[left] + nums[right]
                        if sum == 0:
                            ans.append([num, nums[left], nums[right]])
                            left += 1
                            right -= 1
                            while left < right and nums[left] == nums[left - 1]:
                                left += 1
                            while left < right and nums[right] == nums[right + 1]:
                                right -= 1
                        elif sum > 0:
                            right -= 1
                        else:
                            left += 1

                return ans
                # res = []
                # nums.sort()

                # for i in range(len(nums)):
                #     if i > 0  and nums[i] == nums[i-1]:
                #         continue
                #     left = i + 1
                #     right = len(nums) - 1
                #     while left < right:
                #         total = nums[i] + nums[left] + nums[right]
                #         if total > 0:
                #             right -= 1
                #         elif total < 0:
                #             left += 1
                #         else:
                #             res.append([nums[i], nums[left], nums[right]])
                #             left += 1
                #             while nums[left] == nums[left-1] and left < right :
                #                 left += 1
                # return res

        # res = []
        # for index, num in enumerate(nums):
        #     for i in range(index + 1, len(nums) - 1):
        #         if num + nums[i] + nums[i + 1] == 0:
        #             tmp = [num, nums[i], nums[i + 1]]
        #             if tmp not in res:
        #                 res.append(tmp)
        # return res


        # i, j, k = 0,1,2
        # res = []
        # while k < len(nums):
        #     if nums[i] + nums[j] + nums[k] == 0:
        #         res.append([nums[i],nums[j],nums[k]])
        #     i += 1
        #     j += 1
        #     k += 1
        # return res

my_obj = Solution()
# print(my_obj.threeSum([-100,-70,-60,110,120,130,160]))
print(my_obj.threeSum([-1,0,1,2,-1,-4]))


# def threeSum(self, nums: List[int]) -> List[List[int]]:
#     nums.sort()
#     ans = []
#     for idx, n in enumerate(nums):
#         # duplicate check
#         if idx > 0 and n == nums[idx - 1]:
#             continue
#         l, r = idx + 1, len(nums) - 1
#         while l < r:
#             if n + nums[l] + nums[r] == 0:
#                 ans.append([n, nums[l], nums[r]])
#                 # surpass duplicates
#                 l += 1
#                 r -= 1
#                 while l < r and nums[l - 1] == nums[l]:
#                     l += 1
#                 while l < r and nums[r + 1] == nums[r]:
#                     r -= 1
#
#             elif n + nums[l] + nums[r] > 0:
#                 r -= 1
#             else:
#                 l += 1
#     return ans