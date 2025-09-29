# find the intersection of two arrays:

def intersecting_array(A1, A2):
    res = []
    for elem in A1:
        if elem in A2:
            res.append(elem)
    return res


def find_duplicate(arr):
    seen = {}
    ret = ""
    for elem in arr:
        # print(ret, seen, elem)
        if seen.get(elem) is None:
            seen[elem] = 0
        elif seen.get(elem) >= 0:
            ret = elem
    return ret


# find non duplicate character from string

def ret_non_duplicate(s):
    seen = {}
    for ch in s:
        if ch not in seen:
            seen[ch] = 1
        else:
            seen[ch] = seen[ch] + 1
    for k, v in seen.items():
        if v == 1:
            return k

# print(intersecting_array([1,2,3,4,5],[0,2,4,6,8]))
# print(find_duplicate(["a","b","c","d","c", "e","f"]))
print(ret_non_duplicate("malahlam"))

