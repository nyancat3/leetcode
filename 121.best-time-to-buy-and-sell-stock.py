#
# @lc app=leetcode id=121 lang=python3``
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        while r < len(prices):
            if prices[r] - prices[l] > 0:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r # if there is a cheaper price, move l to the point. so we won't miss the lowest price in the list.
            r += 1
        return profit
# @lc code=end
