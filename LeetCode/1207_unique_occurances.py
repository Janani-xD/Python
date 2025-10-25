from collections import Counter, defaultdict
from typing import List


class UniqueOccurrences:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = defaultdict(int)
        for num in arr:
            counts[num] += 1
        occur = list(counts.values())
        return len(occur) == len(set(occur))

    # def unique_occur(self, nums):
    #     counter = Counter(nums)
    #     print(counter)
    #     s = set()
    #     for v in counter.values():
    #         print(v)
    #         if v in s:
    #             return False
    #         else:
    #             s.add(v)
    #     return  True

my_obj = UniqueOccurrences()
print(my_obj.uniqueOccurrences([1,2,3,4]))
print(my_obj.uniqueOccurrences([1,2,3,4,1,2,3,4,1]))