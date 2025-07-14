from collections import Counter
import heapq


# print(dir(heapq))


heap = [4,10,1,3,0,-4,-10,12]
heapq.heapify(heap)
# print(heap)
heapq.heappush(heap,-13)
# print(heap)
smallest = heapq.heappop(heap)
# print(heap, smallest)
item = heapq.heapreplace(heap,3)
# print(item, heap)


# trick to convert max heap as the heapify functionality only does min heap
a_arr = [-4,3,1,0,2,5,10,8,12,9]
n = len(a_arr)
for i in range(n):
    a_arr[i] = -a_arr[i]

heapq.heapify(a_arr)
largest = -heapq.heappop(a_arr)
# print('a_arr : ' , a_arr)
# print("largest elem in a_arr : ", largest)

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
    """res = []
    heapq.heapify(arr) #O(k)
    print("55 : ", arr)
    for i,elem in enumerate(arr):
        print("57 : ", arr)
        print("58 : ", elem)
        small = heapq.heappop(arr) #O(log k)
        res.append(small)
    print("59 : ", res)
    # return res[-k:]""" # Code that wont work
    res = [0]*k
    for i in range(len(arr)):
        arr[i] = -arr[i]
    print("re-arranged : ", arr)
    heapq.heapify(arr)
    for i in range(k):
        large = -heapq.heappop(arr)
        res[k-1] = large
        k-=1

    return res


# print(k_largest(input, k))


# Problem 3: Top K Frequent Elements
# Given a list of integers and an integer k, return the k frequent elements from the array

# arr = [1, 1, 1, 2, 2, 3]
# k = 2
# Output: [1, 2]

def top_k_elements(arr, k):
    dict1 = {}
    res = []
    for elem in arr:
        # elem_in_str = str(elem)
        if elem not in dict1:
            dict1[elem] = 1
        else:
            count = dict1[elem]
            dict1[elem] = count + 1
        print(elem, dict1)
        if dict1[elem] >= k and elem not in res:
            res.append(elem)
    return  res

# print(top_k_elements([1,1,1,2,2,3],2))

def topKFrequent(nums, k):
    # Step 1: Count the frequency of each element
    freq_map = Counter(nums)
    # Step 2: Build a min-heap of size k using (frequency, number)
    min_heap = []

    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)  # Remove least frequent

    # Step 3: Extract the numbers from the heap
    return [num for freq, num in min_heap]

print(topKFrequent([1,1,1,2,2,3],2))