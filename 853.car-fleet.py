#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs = sorted(pairs, reverse=True) # O(nlogn), sorted by the first element
        stack = []
        for p in pairs:
            hours = (target - p[0]) / p[1]
            if not stack or hours > stack[-1]:
                stack.append(hours)
        return len(stack)

        # Another solution without a stack
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs = sorted(pairs, reverse=True) # O(nlogn), sorted by the first element
        ans = 0
        slowest_hours = 0
        for p in pairs:
            hours = (target - p[0]) / p[1]
            if hours > slowest_hours:
                ans += 1
                slowest_hours = hours
        return ans
# @lc code=end
