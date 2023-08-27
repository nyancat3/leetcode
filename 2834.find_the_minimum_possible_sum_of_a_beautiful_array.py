class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        ans = 1
        ans_set = {1}
        i = 2
        while True:
            if len(ans_set) == n:
                break
            if (target - i) not in ans_set:
                ans_set.add(i)
                ans += i
            i += 1
        return ans
