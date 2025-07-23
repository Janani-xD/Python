from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row = False
        first_col = False

        for row in matrix:
            for element in row:
                print(element)

my_obj = Solution()
print(my_obj.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))