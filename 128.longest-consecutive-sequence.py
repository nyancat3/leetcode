#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for n in nums:
            if (n - 1) not in nums: # Check if it's the start of a consecutive sequence
                len = 1
                while (n + len) in nums:
                    len += 1
                ans = max(ans, len)
        return ans
# @lc code=end
