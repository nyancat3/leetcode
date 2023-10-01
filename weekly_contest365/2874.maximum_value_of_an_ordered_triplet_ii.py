class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_from_left = []
        max_left = -1
        for i in range(len(nums)):
            max_left = max(max_left, nums[i])
            max_from_left.append(max_left)

        max_from_right = []
        max_right = -1
        for i in range(len(nums) - 1, -1, -1):
            max_right = max(max_right, nums[i])
            max_from_right.append(max_right)
        max_from_right.reverse()

        print(max_from_left)
        print(max_from_right)
        ans = 0
        for j in range(1, len(nums) - 1):
            ans = max(ans, (max_from_left[j - 1] - nums[j]) * max_from_right[j + 1])

        return ans
