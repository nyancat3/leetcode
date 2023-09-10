class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        diff_x = abs(fx - sx)
        diff_y = abs(fy - sy)
        diag = min(diff_x, diff_y)
        shortest = diff_x + diff_y - diag

        ans = True
        if shortest == 0 and t == 1:
            ans = False
        else:
            ans = shortest <= t

        return ans
