from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        min_limit = 0
        max_limit = 0
        res = []
        for min, max in intervals:
            print(min, max, min_limit, max_limit)
            if min_limit == 0 and max_limit == 0:
                print("10")
                min_limit = min
                max_limit = max
            elif (min > min_limit and min < max_limit) and (max > max_limit):
                print("14")
                max_limit = max
            elif min == max_limit and max > max_limit:
                print("17")
                max_limit = max
            elif min > min_limit and max == max_limit:
                print("20")
                continue
            elif min > min_limit and min > max_limit or min < min_limit and min < max_limit:
                print("23")
                res.append([min_limit, max_limit])
                min_limit = min
                max_limit = max
            print("27")
        res.append([min_limit, max_limit])
        return res



my_obj = Solution()
# print(my_obj.merge([[1,3],[2,6],[8,10],[15,18]]))
# print(my_obj.merge([[1,4],[4,5]]))
print(my_obj.merge([[1,4],[0,0]]))

