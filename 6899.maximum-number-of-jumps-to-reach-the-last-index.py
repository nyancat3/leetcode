# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/description/
# Dynamic programming
# Time Complexity O(n^2), Space Complexity O(n)
# https://stackoverflow.com/questions/46801171/what-is-the-space-complexity-of-my-python-function
# In python3, range(n) will return an iterator(without creating the whole n-length list), so the space complexity is O(1).
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        maxsteplist = [-1] * n
        maxsteplist[-1] = 0 # get the last element by using -1 as the index value of the list

        for i in range(n - 2, -1, -1): # from n-2 to 0 decreasing
            for j in range(i + 1, n): # from i+1 to n-1
                if (abs(nums[i] - nums[j]) <= target and maxsteplist[j] > -1):
                    maxsteplist[i] = max(maxsteplist[i], maxsteplist[j] + 1)
        return maxsteplist[0]
