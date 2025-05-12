#Brute force solution

'''
The brute force would be to pick every element in the list (i.e. from index 0 to n) and for each index compare it with other elements in the list
TC : O(n^2)
'''
def two_sum_brute(nums : list, Target : int):
    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if i == j :
    #             continue
    #         else:
    #             if (nums[i] + nums[j]) == Target:
    #                 return [i,j]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j]) == Target:
                return [i, j]

#Better solution

'''
The better solution is to make use of an additional data structure like hashmap or dictionaries 
uses the compliment method to find the target from the array/list
TC : Best Case : O(N) extending to O(N^2)
SC : O(1)
'''
def two_sum_better(nums : list, Target : int):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j]) == Target:
                return [i, j]

#Optimal solution
'''
The Optimal solution would be to use the Two pointer method. That shifts based on the value present in the left and 
right index. 
Draw back is the list has to be sorted. With creates a space complexity ofO(N log N) but other wise the TC sticks to 
O(N)

'''
def two_sum_optimal():
    pass

print(two_sum_brute([100,255,8768,85875,8766,7869,3,4534,1231,342354,2,7,11,13], 9))
print(two_sum_better([100,255,8768,85875,8766,7869,3,4534,1231,342354,2,7,11,13], 9))