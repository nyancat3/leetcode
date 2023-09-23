#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_num = nums[0]
        # O(log n)
        while l <= r:
            m = (l + r) // 2
            min_num = min(min_num, nums[m])
            if nums[m] < nums[r]:   # the right side is in ascending order
                r = m - 1
            else:
                l = m + 1
        return min_num
# @lc code=end
