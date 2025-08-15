# two sum

#1 Two Sum

#1 - Two Sum
# Brute Force Solution
def twoSum_bruteforce(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
# Efficient Solution

def twoSum_hashmap(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
# Optimal Approach
# Same as efficient, O(n) time, O(n) space is optimal.


#11 Container with most water


# Brute Force Solution
def maxArea_bruteforce(height):
    max_area = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            max_area = max(max_area, min(height[i], height[j]) * (j-i))
    return max_area

# Efficient Solution
def maxArea_two_pointer(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        return max_area
# Optimal Approach
# Two-pointer method is optimal here, O(n) time, O(1) space.


#26 Remove duplicates from sorted array

# Brute Force Solution

def removeDuplicates_bruteforce(nums):
    nums[:] = sorted(set(nums))
    return len(nums)

# Efficient Solution

def removeDuplicates_two_pointer(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
# Optimal Approach
# Two-pointer method is optimal, O(n) time, O(1) space.

#121 Best time to buy and sell stocks
#217 Contains duplicate
#238 Product of array except self
#53 Maximum subarray (Kadane’s Algorithm)
#53 Three Sum
#56 Merge Intervals
#42 Trapping rain water
