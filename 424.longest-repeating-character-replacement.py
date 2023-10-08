#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans, l = 0, 0
        dict = {}   # { alphabet: count, ... } max length is 26
        for r in range(len(s)):
            dict[s[r]] = dict.get(s[r], 0) + 1
            max_count = max(dict.values())  # O(26)
            current_len = r - l + 1

            while current_len - max_count > k:
                dict[s[l]] -= 1
                l += 1
                max_count = max(dict.values())
                current_len = r - l + 1
            ans = max(ans, current_len)

        return ans
# @lc code=end
