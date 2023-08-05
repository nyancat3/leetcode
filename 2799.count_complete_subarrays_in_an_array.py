# https://leetcode.com/problems/count-complete-subarrays-in-an-array/

# Sliding Window, O(n)
# https://leetcode.com/problems/count-complete-subarrays-in-an-array/solutions/3839312/100-sliding-window-video-counting-complete-subarrays-good-approach/
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        distinct_elements = len(set(nums))
        count = 0
        left = 0
        right = 0
        counter = Counter()

        for right in range(n):
            counter[nums[right]] += 1
            while len(counter) == distinct_elements:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
                count += n - right

        return count
