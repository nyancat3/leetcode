# You are given a 0-indexed integer array nums having length n, an integer indexDifference, and an integer valueDifference.

# Your task is to find two indices i and j, both in the range [0, n - 1], that satisfy the following conditions:

# abs(i - j) >= indexDifference, and
# abs(nums[i] - nums[j]) >= valueDifference
# Return an integer array answer, where answer = [i, j] if there are two such indices, and answer = [-1, -1] otherwise. If there are multiple choices for the two indices, return any of them.

# Note: i and j may be equal.
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        len_n = len(nums)
        for i in range(len_n):
            for j in range(len_n):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]
        return [-1, -1]
