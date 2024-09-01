#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Iterative O(n * 2^n)
        result = [[]]
        for num in nums:
            for i in range(len(result)):
                result.append(result[i] + [num])
        return result

        # DFS / Backtracking O(n * 2^n)
        # For Time it is O(n * 2^n) because there will be 2^n different subsets, and we have to create a copy of each one, which is O(n).
        # For Space it is O(n) if you don't count the output array, because the size of the function call stack will be O(n). Meaning we have to call the recursive function n times in a row, before it returns.
        result = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision not to include nums[i]
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return result

# @lc code=end
