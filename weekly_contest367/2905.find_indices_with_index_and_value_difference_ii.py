class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        min_index = 0
        max_index = 0
        # O(n)
        for i in range(indexDifference, len(nums)):
            # check between 0 to (i - indexDifference)
            if nums[i - indexDifference] < nums[min_index]:
                min_index = i - indexDifference
            if nums[i - indexDifference] > nums[max_index]:
                max_index = i - indexDifference
            print(i, min_index, max_index)
            if nums[i] - nums[min_index] >= valueDifference:
                return [i, min_index]
            if nums[max_index] - nums[i] >= valueDifference:
                return [i, max_index]
        return [-1, -1]
