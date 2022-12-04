#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        # Time O(32) = O(1), Space O(1)
        # result = 0
        # while n:
        #     result += n % 2 # 0 / 1
        #     n = n >> 1  # bit shift to the right
        # return result

        # A little bit efficient solution as we can ignore many zeros
        # Time O(1), Space O(1)
        result = 0
        while n:
            n &= (n - 1)
            result += 1
        return result
# @lc code=end
