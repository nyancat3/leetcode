#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
# Time Complexity: O(n), Memory Complexity: O(n) as we use a hashmap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]   # freq[0] will not be used

        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for f in range(len(freq) - 1, 0, -1):
            for n in freq[f]:   # At most n times in total as values are distinct
                res.append(n)
            if len(res) == k:
                return res
# @lc code=end
