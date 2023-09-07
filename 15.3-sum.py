#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    # O(n log n) + O(n^2) = O(n^2) solution
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(n log n)
        ans = []

        # O(n^2)
        for l in range(len(nums) - 2):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            m, r = l + 1, len(nums) - 1
            while m < r:
                sum = nums[l] + nums[m] + nums[r]
                if sum == 0:
                    ans.append([nums[l], nums[m], nums[r]])
                    print(l, m, r)
                    m += 1
                    while nums[m] == nums[m - 1] and m < r:
                        m += 1
                elif sum > 0:
                    r -= 1
                elif sum < 0:
                    m += 1
        return ans
# @lc code=end
