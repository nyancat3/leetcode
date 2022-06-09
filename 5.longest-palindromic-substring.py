#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(n^2) solution
        # max_len = 0
        # ans = ""
        # for i in range(len(s)): # 0 <= i < len(s)
        #     for j in range(len(s), i, -1): # len(s) >= j > i
        #         substr = s[i:j] # s[i] to s[j-1]
        #         if len(ans) >= j - i: # reduce time
        #             break
        #         if substr == substr[::-1]: # substr[::-1] means reversed(substr)
        #             if len(substr) > max_len:
        #                 max_len = len(substr)
        #                 ans = substr
        # return ans

        # O(n^2) ? but faster than the above one
        res = ""
        for i in range(len(s)): # 0 <= i < len(s)
            odd = self.palindrome(s, i, i)
            even = self.palindrome(s, i, i + 1)
            res = max(res, odd, even, key=len)
        return res

    def palindrome(self, string, left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        left += 1
        right -= 1

        # If an odd case is like left = 3, right = 2, string[3:2] returns empty list [] with no errors
        # Also string[3:3] returns empty list []
        return string[left:right + 1] # from string[0] to string[right]
# @lc code=end
