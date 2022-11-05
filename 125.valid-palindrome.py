#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cheat solution
        # lower_s = s.lower()
        # alnum_s = ""
        # for ls in lower_s:
        #     if ls.isalnum():
        #         alnum_s += ls
        # return alnum_s == alnum_s[::-1]

        # step by step solution
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alnum(s[l]):
                l += 1
            while l < r and not self.alnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def alnum(self, c: str) -> bool:
        return (
            ord('a') <= ord(c) <= ord('z')
            or ord('A') <= ord(c) <= ord('Z')
            or ord('0') <= ord(c) <= ord('9')
        )
# @lc code=end
