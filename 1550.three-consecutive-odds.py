#
# @lc app=leetcode id=1550 lang=python3
#
# [1550] Three Consecutive Odds
#

# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        counter = 0
        for num in arr:
            if num % 2 == 1:
                counter += 1
                if counter == 3:
                    return True
            else:
                counter = 0
        return False

# @lc code=end
