from operator import length_hint


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        W = len(word)

        if m == 1 and n == 1 ## Condition when the matrix has only one row and one coloum and the only word needs to
            # be checked with the word being searched
            return board[0][0] == word

        def backtrack(pos, index):
            i, j = pos

            if index == W:
                return True
            if board[i][j] != word[index]:
                return False

            char = board[i][j]
            board[i][j] = '#' # Temp Change
            for i_off, j_off in [(0,1),(1,0),(0,-1),(-1,0)]: # index for up , down, left and right
                r, c = i + i_off, j + j_off
                if 0 <= r < m and 0 <= c < n:
                    if backtrack((r,c), index+1):
                        return True
            board[i][j] = char # reverts the hash that was being replaced
            return False

        for i in range(m): # Simply the loop used to iterate through every element in the Adjacency Matrix (i is for
            # row)
            for j in range(n): #(j is for col)
                if backtrack((i,j),0): # Back tracking should help the array to be iterated in up , down ,
                    # left and right direction. Usually element in left can be marked as '#" because the condition
                    # does not revisit in backward direction.
                    return True
        return False

    # TC : O((m*n) * (m*n)) ~~ O((m*n)**2)
    # SC = O(L) - L is the length of the search word