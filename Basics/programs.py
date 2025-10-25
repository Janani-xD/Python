def reverse_str(str):
    return str[::-1]


def check_palindrome(str):
    s = str.lower()
    return s == s[::-1]


def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)


def second_largest_elem(arr):
    arr.sort()
    return arr[1]


def second_largest_elem(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr[-2]


def find_freq(str):
    dict = {}
    for word in str.split():
        dict[word] = dict.get(word, 0) + 1
    return dict


def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

    # if n < 2:
    #     return False
    # if num % 2 == 0 and num % 3 == 0:
    #     return False


def fibonacci(n):
    if n == 0 or n == 1:
        print(n)
    else:
        a = 0
        b = 1
        res = 0
        print(a, end=" ")
        print(b, end=" ")
        for i in range(2, n):
            res = a + b
            print(res, end=" ")
            a, b = b, res

def find_pair(arr, target):
    res = set()
    left = 0
    for number1 in arr:
        print("73 : ", left, number1, res)
        if target - arr[left] == number1:
            res.add((number1, arr[left]))
            left += 1


# print(reverse_str("Hello"))
# print(check_palindrome("janani"))
# print(fact(10))
# print(second_largest_elem([100, 200, 4]))
# print(second_largest_elem([1, 2, 5]))
# print(find_freq("python is great and python is fun"))
# fibonacci(100)
# print(is_prime(40))
print(find_pair([1,3,2,2,4,0],4))