#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # O(log n)
        while l <= r:
            m = (l + r) // 2
            print(l, m, r)
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:  # m is in the left sorted portion
                if nums[l] <= target <= nums[m]:  # if the target is in the current portion
                    r = m - 1   # move to the left
                else:
                    l = m + 1   # move to the right
            else:   # m is in the right sorted portion
                if nums[m] <= target <= nums[r]:  # if the target is in the current portion
                    l = m + 1   # move to the right
                else:
                    r = m - 1   # move to the left
        return -1

# @lc code=end
