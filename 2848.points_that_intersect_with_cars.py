class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        set_num = set()
        for num in nums:
            for i in range(num[0], num[1] + 1):
                set_num.add(i)
        return len(set_num)
