#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, ans = [], [0 for _ in range(len(temperatures))]  # [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                latest_i, latest_t = stack.pop()    # assignment unpacking
                ans[latest_i] = i - latest_i    # number of days
            stack.append((i, temperature))
        return ans

# @lc code=end
