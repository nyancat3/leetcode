class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_from_right = []
        max_right = -1
        for i in range(len(nums) - 1, -1, -1):
            max_right = max(max_right, nums[i])
            max_from_right.append(max_right)
        max_from_right.reverse()

        ans = 0
        max_from_left = [nums[0]]
        max_left = nums[0]
        for i in range(1, len(nums) - 1):
            max_left = max(max_left, nums[i])
            max_from_left.append(max_left)
            ans = max(ans, (max_from_left[i - 1] - nums[i]) * max_from_right[i + 1])
        return ans
