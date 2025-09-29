# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
def pattern_1(n):
    for i in range(1,n + 1):
        for j in range(i):
            print(i, end = ' ')
        print()


# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1

def pattern_2(n):
    for i in range(1,n+ 1):
        print(str(n) * i, end=' ')
        n -= 1
        print()


# 0
# 2 2
# 4 4 4
# 6 6 6 6
# 8 8 8 8 8

def pattern_3(n):
    m = 0
    i = 1
    while m < (2 * n):
        print(str(m) * i, end=' ')
        print()
        m += 2
        i += 1
# 1
# 2 2
# 1 1 1
# 2 2 2 2
# 1 1 1 1 1

def pattern_4(n):
    for i in range(1, n+1):
        for j in range(i):
            if i % 2 == 0:
                print(2, end=' ')
            else:
                print(1, end=' ')
        print()

#         1
#       2 2 2
#     3 3 3 3 3
#   4 4 4 4 4 4 4
# 5 5 5 5 5 5 5 5 5
#   6 6 6 6 6 6 6
#     7 7 7 7 7
#       8 8 8
#         9

def pattern_5(n):
    counter = 1
    for i in range(1, n + 1):
        for j in range(counter):
            print(i, end = ' ')
        print()
        counter += 2
    counter -= 4
    for i in range(n + 1, (2*n) + 1):
        for j in range(counter):
            print(i, end=' ')
        print()
        counter -= 2

# pattern_1(5)
# pattern_2(5)
# pattern_3(5)
# pattern_4(5)
pattern_5(5)