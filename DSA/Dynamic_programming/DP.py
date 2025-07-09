# LeetCode climbing stair

# Using memoization

def climbstairs(N):
    dp = [0] * (N+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]

# Using constant space

def climbStairs(self, n: int) -> int:
    if n <= 3:
        return n
    prev1 = 3
    prev2 = 2
    curr = 0
    for i in range(3, n):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return curr


# LeetCode House Robber - 198


def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    dp = [0] * len(nums)
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2]+ nums[i])
    return dp[-1]

    def rob_rec(self, nums: List[int]) -> int: ### Exceeds the time limit
        # Recursive solution
        # Time O(2^n)
        # Space O(n)

        n = len(nums)

        def helper(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            return max(nums[i] + helper(i - 2), helper(i - 1))

        return helper(n - 1)

    def rob_tp(self, nums):
        # Top Down DP (Memoized)
        # Time O(n)
        # Space O(n)

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2
            return max(nums[0], nums[1])

        def helper(i):
            return max(nums[i]+ helper(i-2), helper(i-1))
        return helper(n-1)

    def rob_bu(self, nums):
        # Bottom up DP (Tabulation)
        # Time O(n)
        # Space O(n)

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2
            return max(nums[0], nums[1])
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp(n-1)

    def rob_CS(self, nums):
        # Bottom up DP (Constant Space)
        # Time O(n)
        # Space O(1)

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2
            return max(nums[0], nums[1])
        prev = = nums[0]
        curr = max(nums[0], nums[1])
        for i in range(2, n):
            prev , curr = curr, max(nums[i] + prev, curr)
        return dp(n-1)

    # LeetCode Min Code Climbing stairs - 746

    def minCostClimbingStairs(cost):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

        def rob_rec(self, nums: List[int]) -> int:  ### Exceeds the time limit
            # Recursive solution
            # Time O(2^n)
            # Space O(n)

            n = len(nums)

            def helper(i):
                if i == 0:
                    return nums[0]
                if i == 1:
                    return max(nums[0], nums[1])
                return max(nums[i] + helper(i - 2), helper(i - 1))

            return helper(n - 1)

        def rob_tp(self, nums):
            # Top Down DP (Memoized)
            # Time O(n)
            # Space O(n)

            n = len(nums)
            if n == 1:
                return nums[0]
            if n == 2
                return max(nums[0], nums[1])

            def helper(i):
                return max(nums[i] + helper(i - 2), helper(i - 1))

            return helper(n - 1)

        def rob_bu(self, cost):
            # Bottom up DP (Tabulation)
            # Time O(n)
            # Space O(n)

            n = len(cost)

            dp = [0] * (n+1)

            for i in range(2, n+1):
                dp[i] = min(cost[i-2] + dp[i - 2], dp[i - 1] + cost[i-1])
            return dp(n)

        def minCostClimbingStairs_CS(self, cost):
            # Bottom up DP (Constant Space)
            # Time O(n)
            # Space O(1)

            n = len(cost)
            prev = curr = 0,0
            for i in range(2, n+1):
                prev, curr = curr, min(cost[i-2] + prev, cost[i-1] + curr)
            return dp(n)