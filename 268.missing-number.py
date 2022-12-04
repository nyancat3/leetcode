#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Efficient solution 1 - xor: Time O(n), Space O(1)
        result = len(nums)  # Add the last num beforehand
        for i in range(len(nums)):  # 0 to len(nums) - 1
            result ^= i ^ nums[i]
        return result

        # Efficient solution 2 - sum: Time O(n), Space O(1)
        # result = len(nums)  # Add the last num beforehand
        # for i in range(len(nums)):  # 0 to len(nums) - 1
        #     result += (i - nums[i])
        # return result

        # Brute force solution: Time Average O(n), Worst O(n^2), Space O(n)
        # numsSet = set(nums) # Convert list to set: O(n)
        # for i in range(len(nums) + 1):  # 0 to len(nums)
        #     if not i in numsSet:    # Average O(1), Worst O(n)
        #         return i
# @lc code=end
