#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # collections_mag = collections.Counter(magazine)
        # collections_ran = collections.Counter(ransomNote)
        # for key in collections_ran:
        #     if collections_ran[key] > collections_mag[key]:
        #         return False
        # return True
        return not collections.Counter(ransomNote) - collections.Counter(magazine) # O(m+n)
# @lc code=end
