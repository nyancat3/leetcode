#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dictionary (hash map) T O(s + t), M O(s + t)
        if len(s) != len(t):
            return False
        s_dict, t_dict = dict(), dict()
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1
        for key in s_dict:
            if s_dict[key] != t_dict.get(key, 0):
                return False
        return True

        # counter (hash map) T O(s + t), M O(s + t)
        return Counter(s) == Counter(t)

        # sorted T O(n log n), M worst O(n), best O(1)
        return sorted(s) == sorted(t)
# @lc code=end
