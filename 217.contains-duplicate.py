#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Use set instead of dict
        # T O(n), S O(n)
        hash_set = set()
        for n in nums:
            if n in hash_set: # T O(1) * n = O(n)
                return True
            hash_set.add(n)
        return False
# @lc code=end
