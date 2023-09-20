#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_bananas = max(piles)
        if h == len(piles):
            return max_bananas

        ans = max_bananas
        l, r = max(1, max_bananas // h), max_bananas
        # O(log(max(p)) * p)
        while l <= r:
            m = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)
            if hours <= h:
                ans = min(ans, m)
                r = m - 1
            else:
                l = m + 1
        return ans

# @lc code=end
