class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Time complexity: O(2n) = O(n)
        def dominant_num(nums: List[int]) -> Tuple[int, int]:
            n_dict = dict()
            dominant = 0
            for i in range(len(nums)):
                n_dict[nums[i]] = n_dict.get(nums[i], 0) + 1
                if n_dict[nums[i]] > len(nums) // 2:
                    dominant = nums[i]
            return dominant, n_dict.get(dominant, 0)

        dominant, dom_freq = dominant_num(nums)
        num_of_dom = 0
        for i in range(len(nums)):
            if nums[i] == dominant:
                num_of_dom += 1
                if num_of_dom > (i + 1) // 2 and (dom_freq - num_of_dom) > (len(nums) - i - 1) // 2:
                    return i
        return -1
