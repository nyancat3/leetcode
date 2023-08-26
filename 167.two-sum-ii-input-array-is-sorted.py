#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        for l in range(len(numbers)):
            while (numbers[l] + numbers[r]) > target :
                r -= 1
            if (numbers[l] + numbers[r]) == target:
                return [l + 1, r + 1]
# @lc code=end
