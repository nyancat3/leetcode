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
        max_count = 0
        # O(n)
        for r in range(len(s)):
            dict[s[r]] = dict.get(s[r], 0) + 1
            max_count = max(max_count, dict[s[r]])
            current_len = r - l + 1

            if current_len - max_count > k:
                dict[s[l]] -= 1
                l += 1
                # no need to decrease max_count as the size of the window will be the same as long as both l and r are increasing at the same time
            else:
                ans = max(ans, current_len)

        return ans
# @lc code=end
