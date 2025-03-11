def isPrime(self, n: int) -> bool:
        # Your code here
        if n == 2 or n == 3 or n == 5 or n == 7:
            return True
        while n > 7:
            if n% 2 == 0 or n % 3 == 0:
                return False
            return True
        return False
def is_prime1(Num):
        if Num <= 1:
                return False
        else:
                is_prime = True
                for i in range(2, Num):
                        if (Num % i) == 0:
                                is_prime = False
                                break
                return is_prime
                
                
