#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index_by_c = {}
        for i, c in enumerate(s):
            last_index_by_c[c] = i

        c_set = set()
        ans = ""
        for i, c in enumerate(s):
            if not c in c_set:  # avg O(1)
                while ans and ord(ans[-1]) > ord(c) and last_index_by_c[ans[-1]] > i:
                    c_set.remove(ans[-1])
                    ans = ans[:len(ans) - 1]
                ans += c
                c_set.add(c)

        return ans
# @lc code=end
