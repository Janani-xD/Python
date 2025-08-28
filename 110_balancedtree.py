# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def isBalanced(self, root) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            print(left, right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]




obj1 = Solution()
root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(3)
n5 = TreeNode(4)
n6 = TreeNode(4)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n3.left = n5
n3.right = n6

# obj1.isBalanced([1,2,2,3,3,None,None, 4,4])
print(obj1.isBalanced(root))