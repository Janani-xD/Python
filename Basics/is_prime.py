def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(23))


# import math
#
# n = 10
#
# if n < 2:
#     print("not PRIME")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("not PRIME")
#             break
#     else:
#         print("PRIME")
#
#
# def is_prime(num):
#     if num < 2:
#         return False
#     if n % 2 == 0:
#         return n == 2
#     for i in range(3, int(math.sqrt(num)) + 1, 2):
#         if n % i == 0:
#             return False
#     return True
#
#
# print(is_prime(23))
# # def isPrime(self, n: int) -> bool:
# #         # Your code here
# #         if n == 2 or n == 3 or n == 5 or n == 7:
# #             return True
# #         while n > 7:
# #             if n% 2 == 0 or n % 3 == 0:
# #                 return False
# #             return True
# #         return False
#
# # def is_prime1(Num):
# #         if Num <= 1:
# #             return False
# #         else:
# #             is_prime = True
# #             for i in range(2, Num):
# #                 if (Num % i) == 0:
# #                     is_prime = False
# #                     break
# #             return is_prime
#
#
