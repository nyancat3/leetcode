import statistics

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        nums.sort()
        middle = int(statistics.median(nums))
        ans = 1e15
        if self.isPalindrome(middle):
            ans = self.cost(nums, middle)

        low, high = middle - 1, middle + 1
        left, right = -1, -1
        while left == -1 or right == -1:
            if left == -1 and self.isPalindrome(low):
                left = low
            if right == -1 and self.isPalindrome(high):
                right = high
            low -= 1
            high += 1

        return min(ans, min(self.cost(nums, right), self.cost(nums, left)))

    def isPalindrome(self, num: int) -> bool:
        num_copy = num
        reversed_num = 0
        while num_copy > 0:
            reversed_num = reversed_num * 10 + num_copy % 10
            num_copy //= 10
        return reversed_num == num

    def cost(self, nums: List[int], x) -> int:
        res = 0
        for n in nums:
            res += abs(n - x)
        return res
