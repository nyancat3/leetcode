#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        # O(n) solution
        dp = [0] * (n + 1)  # whichever's fine
        # dp = [0]  # whichever's fine
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
            # dp.append(1 + dp[i - offset])
        return dp

        # Brute Force Time Complexity O(n log n)
        # res = []
        # for i in range(n + 1):
        #     numBit = 0
        #     while i:
        #         numBit += i % 2
        #         i = i >> 1
        #     res.append(numBit)
        # return res
# @lc code=end
