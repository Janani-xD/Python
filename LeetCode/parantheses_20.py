class Solution:
    def isValid(self, s: str) -> bool:
        result = self.add_to_map(s)
        return self.result(result)

    def result(self, res):
        print(res.items())
        for item,count in res.items():
            print(item, count)
            if count % 2 == 0:
                continue
            else:
                return False
        return True
            #return False if item % 2 == 0 else True

    def add_to_map(self, s):
        res = {}
        for element in s:
            if element not in res:
                res[element] = 1
            else:
                #count = res[element]
                res[element] = res[element] + 1
        return res


obj = Solution()
print(obj.isValid("[][[[[]]]]"))