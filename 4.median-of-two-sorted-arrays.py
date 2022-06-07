#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # import statistics # python 3 includes statistics and math by default
        # import math

        return statistics.median(nums1 + nums2)
# @lc code=end
