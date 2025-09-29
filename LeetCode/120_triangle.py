
class Solution:
    def minimumTotal(self, triangle) -> int:
        dp = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            # print('row : ', row)
            # print('dp  : ', dp)
            for i, n in enumerate(row):
                print(f"dp[{i}] : {dp[i]}")
                dp[i] = n + min(dp[i], dp[i+1])
        return dp[0]

my_obj = Solution()
print(my_obj.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])) # output = 11