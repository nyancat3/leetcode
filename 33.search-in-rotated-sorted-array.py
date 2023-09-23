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
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r

            if nums[m] > target:    # wanna find smaller values
                if nums[m] < nums[r]: # the pivot exists in the left part, the right side is in ascending order
                    r = m - 1   # move to the left
                else:   # the pivot exists in the right part, the left side is in ascending order
                    if nums[l] < target < nums[m]:
                        r = m - 1   # move to the left
                    else:
                        l = m + 1   # move to the right
            else:   # wanna find bigger values
                if nums[m] < nums[r]: # the pivot exists in the left part, the right side is in ascending order
                    if nums[m] < target < nums[r]:
                        l = m + 1   # move to the right
                    else:
                        r = m - 1    # move to the left
                else:   # the pivot exists in the right part, the left side is in ascending order
                    l = m + 1   # move to the right
        return -1

# @lc code=end
