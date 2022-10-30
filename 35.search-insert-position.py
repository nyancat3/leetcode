#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            middle_index = (l + r) // 2
            middle_val = nums[middle_index]
            if target == middle_val:
                return middle_index

            if target < middle_val:
                r = middle_index - 1
            else:
                l = middle_index + 1

        return l
# @lc code=end
