#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_set = set()
        l, ans = 0, 0
        c_set.add(s[l])
        for r in range(len(s)):
            while s[r] in c_set:
                c_set.remove(s[l])
                l += 1
            c_set.add(s[r])
            ans = max(ans, len(c_set))
        return ans
        # @lc code=end
