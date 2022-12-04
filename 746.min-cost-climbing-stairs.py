#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):  # stop: position to stop (not included)
            cost[i] += min(cost[i + 1], cost[i + 2])
            print(cost[i])

        return min(cost[0], cost[1])
# @lc code=end
