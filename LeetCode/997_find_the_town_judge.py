class Solution:
    def findJudge(self, n, trust):
        mapping = {i:[] for i in range(1, n + 1)}
        for A, B in trust:
            temp = mapping.get(A, [])
            temp.append(B)
            mapping[A] = temp
        # print(mapping)
        judge = mapping[1]
        # print(judge)
        for i in range(1,n + 1):
            print(i)
            print('13 ', judge)
            print('14 ', mapping[i])
            print('15 ',judge != mapping[i])
            if judge != mapping[i] and mapping[i] != []:
                return -1
        return judge[0]


my_obj = Solution()
# print(my_obj.findJudge(3, [[1,3],[2,3]]))
print(my_obj.findJudge(3, [[1,3],[2,3],[3,1]]))