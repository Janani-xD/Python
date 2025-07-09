import heapq


# print(dir(heapq))


heap = [4,10,1,3,0,-4,-10,12]
heapq.heapify(heap)
print(heap)
heapq.heappush(heap,-13)
print(heap)
smallest = heapq.heappop(heap)
print(heap, smallest)
item = heapq.heapreplace(heap,3)
print(item, heap)


# trick to convert max heap as the heapify functionality only does min heap
a_arr = [-4,3,1,0,2,5,10,8,12,9]
n = len(a_arr)
for i in range(n):
    a_arr[i] = -a_arr[i]

heapq.heapify(a_arr)
print('a_arr : ' , a_arr)

# Problem 1: Find the K Smallest Elements
# Given a list of integers and an integer k, return the k smallest elements in ascending order.

# arr = [7, 10, 4, 3, 20, 15]
# k = 3
# Output: [3, 4, 7]

# sol - using sorting causing a time Complexity of O(n log n)
def k_smallest(arr:list, k:int):
    heapq.heapify(arr) # this does not sort the array everytime
    res = []
    for i,elem in enumerate(arr):
        if i == k:
            return
        small = heapq.heappop(arr)
        # print("small : ", small)
        res.append(small)
    print("res : ", res)
    return res



input = [7, 10, 4, 3, 20, 15]
k = 3
# print(k_smallest(input, k))

# Problem 2: Find the K Largest Elements
# Given a list of integers and an integer k, return the k largest elements in ascending order.

# arr = [7, 10, 4, 3, 20, 15]
# k = 3
# Output: [10, 15, 20]


def k_largest(arr:list, k:int):
    res = []
    heapq.heapify(arr) #O(k)
    print("55 : ", arr)
    for i,elem in enumerate(arr):
        print("57 : ", arr)
        print("58 : ", elem)
        small = heapq.heappop(arr) #O(log k)
        res.append(small)
    print("59 : ", res)
    # return res[-k:]

print(k_largest(input, k))