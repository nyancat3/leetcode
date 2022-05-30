#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#

# @lc code=start
class Solution:
    def numberOfSteps(self, num: int) -> int:
        answer = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            answer += 1
        return answer

# @lc code=end
