#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time Complexity O(logN), Space Complexity O(1)
        # The space complexity will be O(1) because we need two variable to keep track of the range of elements that are to be checked. No other data is needed.
        # In a recursive implementation of Binary Search, the space complexity will be O(logN).
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else: # It is better for micro optimization to check equality of nums[mid] to target in the last order, because the most probable result of this operation will be False, and it slightly increases cpu time.
                return m

        return -1
# @lc code=end
