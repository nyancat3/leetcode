class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        # Iterate backwards
        for i in range(len(nums) - 2, -1, -1):  # len(nums) - 2..0
            if nums[i] <= nums[i + 1]:
                nums[i] += nums[i + 1]
        return nums[0]  # The first element will be the maximum
