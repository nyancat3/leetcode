class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        ans = [[nums[0]]]
        first_val = nums[0]
        for i in range(1, len(nums)):
            if len(ans[-1]) == 3:
                first_val = nums[i]
                ans.append([nums[i]])
            elif nums[i] - first_val > k:
                return []
            else:
                ans[-1].append(nums[i])
        return ans
