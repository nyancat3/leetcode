#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution in O(n^2)
        # if len(nums) == 2:
        #     return [0, 1]
        # for i, num in enumerate(nums): # O(n)
        #     if target - num in nums[i + 1:]: # O(n)
        #         return [i, i + 1 + nums[i + 1:].index(target - num)]

        # Solution in O(n)
        dict = {}
        for i, num in enumerate(nums): # O(n)
            sub = target - num
            if sub not in dict: # O(1) because a dictionary is a hash table
                dict[num] = i
            else:
                return [i, dict[sub]]
# @lc code=end
