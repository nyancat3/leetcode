# Weekly Contest 368 Q2
# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/description/
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        left_min_plus_current = nums.copy()
        left_min = nums[0]
        for i in range(len(nums) - 1):
            left_min = min(left_min, nums[i])
            if left_min < nums[i + 1]:
                left_min_plus_current[i + 1] += left_min
            else:
                left_min_plus_current[i + 1] = -1
        # print(left_min_plus_current)

        ans = sys.maxsize
        right_min = nums[-1]
        for i in range(len(nums) - 1, 1, -1):   # i >= 2
            right_min = min(right_min, nums[i])
            if left_min_plus_current[i - 1] == -1:
                continue
            if right_min < nums[i - 1]:
                ans = min(ans, left_min_plus_current[i - 1] + right_min)
                # print(i, right_min)
                # print(left_min_plus_current[i - 1] + right_min)
        return -1 if ans == sys.maxsize else ans
