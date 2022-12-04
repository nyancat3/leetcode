#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        sums = set()
        while n not in sums:
            sums.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False

    def sumOfSquares(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2  # squared
            output += digit
            n = n // 10
        return output
# @lc code=end
