#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
from collections import defaultdict
import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}  # { character: count, ... }
        for c in s1:
            s1_dict[c] = s1_dict.get(c, 0) + 1
        s1_dict = dict(sorted(s1_dict.items()))
        print(s1_dict)

        current_s2_dict = {}  # { character: count, ... }
        l = 0
        for r in range(len(s2)):
            current_s2_dict[s2[r]] = current_s2_dict.get(s2[r], 0) + 1
            print(current_s2_dict)
            if s1_dict.get(s2[l], 0) == 0:
                current_s2_dict[s2[l]] = current_s2_dict.get(s2[l], 0) - 1
                if current_s2_dict[s2[l]] == 0:
                    del current_s2_dict[s2[l]]
                l += 1
            elif r - l + 1 == len(s1):
                current_s2_dict = dict(sorted(current_s2_dict.items()))
                if current_s2_dict == s1_dict:
                    return True
                else:
                    current_s2_dict[s2[l]] = current_s2_dict.get(s2[l], 0) - 1
                    if current_s2_dict[s2[l]] == 0:
                        del current_s2_dict[s2[l]]
                    l += 1
        return False
# @lc code=end
