""" How to solve this is that we consider each number to be the root element at some point of time and multiply the
left and right subtree for combinations"""

class Solution:
    def numTrees(self, n: int) -> int:
        #numTree[4] = numTrees[0] * numTree[3] +
                    #    numTree[1] * numTree[2] +
                    #    numTree[2] * numTree[1] +
                    #    numTree[3] * numTree[1]
        numTree = [1] * (n + 1)
        # 0 node = 1 Tree
        # 1 node = 1 Tree
        for nodes in range(2, n + 1): # wont run when n is 0 or 1
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                total += numTree[left] * numTree[right]
            numTree[nodes] = total
        return numTree[n]

my_obj = Solution()
print(my_obj.numTrees(0))