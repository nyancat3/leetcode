# https://leetcode.com/contest/weekly-contest-358/problems/max-pair-sum-in-an-array/
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = -1
        max_by_digit = defaultdict(int)  # {'7': 71, '5': 51, ...}
        for num in nums:
            max_digit = max([c for c in str(num)])  # time complexity of max(): O(n)
            if max_digit in max_by_digit:
                ans = max(ans, max_by_digit[max_digit] + num)
            max_by_digit[max_digit] = max(max_by_digit[max_digit], num)
        return ans
