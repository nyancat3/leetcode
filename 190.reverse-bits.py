#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        # Time Complexity O(32) = O(1), Space Complexity O(1)
        res = 0 # 000...0
        for i in range(32): # 0 to 31
            nLastBit = (n >> i) & 1  # 0 or 1: 000...001
            nLastBitReversed = nLastBit << (31 - i)    # reverse nLastBit: 100...000
            res |= nLastBitReversed  # 0 or 1
        return res
# @lc code=end
