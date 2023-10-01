class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        len_n = len(nums)
        ans = 0
        for i in range(len_n - 2):
            for j in range(i + 1, len_n - 1):
                for k in range(j + 1, len_n):
                    ans = max(ans, (nums[i] - nums[j]) * nums[k])
        return ans
