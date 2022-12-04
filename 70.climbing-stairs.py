#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # Dynamic programming - bottom up

        # Time complexity O(n) as we look through the elements once
        # Space complexity O(1) as just using two variables
        one, two = 1, 1 # the number of ways to reach the goal. if it's already the goal, stay there is the choice so twoStep = 1

        for i in range(n - 1):
            currentWays = one + two
            two = one
            one = currentWays

        return one
# @lc code=end
