"""
Problem :
To find all the subsets in the array without duplicates:

Eg Input : [1,2,3]
Output : [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]] # has 2 power 3 solutions

to solve using backtracking


"""

class Solution:
    def subset(self,nums):
        n = len(nums)
        res, sol = [], []

        def backtracking(i):
            print("19", i, res, sol)
            if i == n:
                res.append(sol[:])
                return
            # dont pick nums[i]
            print("23")
            backtracking(i+1)

            # pick nums[i]
            print(f"28 i : {i}")
            sol.append(nums[i])
            print(f"30 sol : {sol}")
            backtracking(i+1)
            print("32")
            sol.pop()
            print(f"34 sol : {sol}")
        print("35")
        backtracking(0)
        return res


my_obj = Solution()
print(my_obj.subset([1,2,3]))



""" i=0, sol=[]
│
├── don't pick nums[0] (1) → backtracking(1, [])
│   │
│   ├── don't pick nums[1] (2) → backtracking(2, [])
│   │   │
│   │   ├── don't pick nums[2] (3) → backtracking(3, [])
│   │   │       (BASE CASE) → append [] to res
│   │   │
│   │   └── pick nums[2] (3) → sol=[3] → backtracking(3, [3])
│   │           (BASE CASE) → append [3] to res
│   │
│   └── pick nums[1] (2) → sol=[2] → backtracking(2, [2])
│       │
│       ├── don't pick nums[2] (3) → backtracking(3, [2])
│       │       (BASE CASE) → append [2] to res
│       │
│       └── pick nums[2] (3) → sol=[2, 3] → backtracking(3, [2, 3])
│               (BASE CASE) → append [2, 3] to res
│
└── pick nums[0] (1) → sol=[1] → backtracking(1, [1])
    │
    ├── don't pick nums[1] (2) → backtracking(2, [1])
    │   │
    │   ├── don't pick nums[2] (3) → backtracking(3, [1])
    │   │       (BASE CASE) → append [1] to res
    │   │
    │   └── pick nums[2] (3) → sol=[1, 3] → backtracking(3, [1, 3])
    │           (BASE CASE) → append [1, 3] to res
    │
    └── pick nums[1] (2) → sol=[1, 2] → backtracking(2, [1, 2])
        │
        ├── don't pick nums[2] (3) → backtracking(3, [1, 2])
        │       (BASE CASE) → append [1, 2] to res
        │
        └── pick nums[2] (3) → sol=[1, 2, 3] → backtracking(3, [1, 2, 3])
                (BASE CASE) → append [1, 2, 3] to res
"""