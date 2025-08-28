class TreeNode:
    def __init__(self, value):
        self.root = value
        self.left = None
        self.right = None


class Solution:
    def sorted_arr_to_bst(self, nums):

        def helper(l,r):
            if l > r:
                return None
            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)
            return root

        return helper(0, len(nums) - 1)

my_obj = Solution()
print(my_obj.sorted_arr_to_bst([-10,-3,0,5,9]))