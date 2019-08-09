class Solution:
    def countPrimes(self, n):
        primes = [True] * n

        i = 2
        while i * i < n:
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
            i += 1
        
        res = 0 
        for i in range(2, n):
            if primes[i]:
                res += 1
        return res