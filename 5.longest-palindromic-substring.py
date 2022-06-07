#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(n^2) solution
        max_len = 0
        ans = ""
        for i in range(len(s)): # 0 <= i < len(s)
            for j in range(len(s), i, -1): # len(s) >= j > i
                substr = s[i:j] # s[i] to s[j-1]
                if substr == substr[::-1]: # substr[::-1] means reversed(substr)
                    if len(substr) > max_len:
                        max_len = len(substr)
                        ans = substr
        return ans
# @lc code=end
