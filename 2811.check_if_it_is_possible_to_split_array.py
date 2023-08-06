# Weekly Contest 357 - Medium
# https://leetcode.com/problems/check-if-it-is-possible-to-split-array/
class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        if len(nums) <= 2:
            return True
        for i in range(len(nums) - 1):
            sum = nums[i] + nums[i + 1]
            if sum >= m:
                return True
        return False
