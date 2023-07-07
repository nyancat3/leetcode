#
# @lc app=leetcode id=2761 lang=python3
#
# [2761] Prime Pairs With Target Sum
#

# @lc code=start
class Solution:
    # Sieve Eratosthenes Algorithms + Two sum
    # https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/
    # https://leetcode.com/problems/prime-pairs-with-target-sum/solutions/3707394/python-3-sieve-eratosthenes-algorithms-two-sum/
    def findPrimePairs(self, n: int) -> List[List[int]]:
        res = []
        primes = [True for i in range(n + 1)]
        # boolean array
        p = 2
        while (p * p <= n):
            # If primes[p] is not changed, then it is a prime
            if (primes[p] == True):
                # Updating all multiples of p
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1

        for p in range(2, n // 2 + 1):
            if primes[p] and primes[n - p]:
                res.append([p, n - p])
        return res
# @lc code=end
