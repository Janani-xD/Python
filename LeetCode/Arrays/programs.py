from collections import defaultdict, Counter


def return_elems(arr):
    lookup = defaultdict(int)
    result = set()
    for elem in arr:
        lookup[elem] += 1
        if lookup[elem] > 1:
            result.add(elem)
    return list(result)

def return_max_occurances(arr):
    # mappings = defaultdict(int)
    # for elem in arr:
    #     mappings[elem] += 1
    # return max(mappings, key=mappings.get)

    count = Counter(arr)
    print(count.most_common(1)[0][0])

def find_missing_number(nums):
    # Using Sum's formula
    # n = len(nums)
    # expected_sum = n * (n + 1) // 2
    # return expected_sum - sum(nums)
    # Using Sum's formula

    # Using XOR Logic
    n = len(nums)
    xor_all = xor_num = 0
    for i in range(n + 1):
        xor_all ^= i
    for num in nums:
        xor_num ^= num
    return xor_all ^ xor_num
    # Using XOR Logic

    # n = len(nums) + 1
    # for i in range(n):
    #     if i not in nums:
    #         return i

def move_zeroes(num):
    left = 0
    for right in range(len(num)):
        if num[right] != 0:
            num[left], num[right] = num[right], num[left]
            left += 1
    return num

# Alternative
def move_zeroes1(nums):
    return [x for x in nums if x != 0] + [0] * nums.count(0)

print(return_elems([4, 3, 2, 7, 8, 2, 3,2, 1]))
print(return_max_occurances([1, 2, 2, 3,3,3,3,3, 1, 4, 2])) # op = 2 because it occurs 3 times
print(find_missing_number([0,1,2,3,4,6]))
print(move_zeroes([0, 1, 0, 3, 12]))
print(move_zeroes1([0, 1, 0, 3, 12]))
