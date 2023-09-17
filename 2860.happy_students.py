class Solution:
    def countWays(self, nums: List[int]) -> int:
        ans = 1 # select all students
        nums = sorted(nums)
        n = len(nums)
        selected_students_num = 0
        if nums[0] > 0:
            ans += 1 # select no student
        for i in range(n - 1): # skip the last student bc selecting all students has already been counted
            selected_students_num += 1 # select nums[i] as well
            if selected_students_num > nums[i] and selected_students_num < nums[i + 1]:
                    ans += 1
        return ans
