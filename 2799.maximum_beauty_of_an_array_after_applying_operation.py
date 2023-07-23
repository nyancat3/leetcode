# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/description/
# sliding windows

# intuitive solution
# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/solutions/3772327/why-and-how-of-the-solution/
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort() # ascending sort O(NlogN)
        i, ans = 0, 0
        for j in range(len(nums)):
            if nums[j] - nums[i] > k * 2:
                i += 1  # while window is not valid increase the current minimum
            else:
                ans = max(ans, j - i + 1)   # current window is valid so update the answer
        return ans
