# Weekly Contest 357 - Easy
# https://leetcode.com/problems/faulty-keyboard/
class Solution:
    def finalString(self, s: str) -> str:
        ans = ''
        for c in s:
            if c == 'i':
                ans = ans[::-1]
            else:
                ans += c
        return ans
