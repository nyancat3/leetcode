# daily q
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/?envType=daily-question&envId=2024-01-04
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num_count = {} # { 0: 4, 1: 2, 2: 2, ... }
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        ans = 0
        for num in num_count:
            if num_count[num] == 1:
                return -1
            ans += num_count[num] // 3
            if num_count[num] % 3 > 0:
                ans += 1
        return ans
