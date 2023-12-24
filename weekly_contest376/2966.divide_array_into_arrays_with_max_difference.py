class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums) < 3:
            return []
        ans = []
        nums.sort()
        first_val = nums[0]
        for i in range(len(nums)):
            if len(ans) > 0 and len(ans[-1]) == 3:
                first_val = nums[i]
                ans.append([nums[i]])
            elif nums[i] - first_val > k:
                return []
            else:
                if len(ans) > 0:
                    ans[-1].append(nums[i])
                else:
                    ans.append([nums[i]])
        return ans
