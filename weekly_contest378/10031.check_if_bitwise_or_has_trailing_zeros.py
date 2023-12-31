class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        even = False
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                if even:
                    return True
                else:
                    even = True
        return False
