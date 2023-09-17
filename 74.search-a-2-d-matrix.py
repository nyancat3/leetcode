#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1d list O(log(m * n))
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = (l + r) // 2
            y = m // COLS
            x = m % COLS
            print(l, r, m)
            if matrix[y][x] < target:
                l = m + 1
            elif matrix[y][x] > target:
                r = m - 1
            else:
                return True
        return False

        # 2d list O(log(m)) + O(log(n)) = O(log(m * n))
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        if top > bottom:
            return False
        # print(row)
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            m = (l + r) // 2
            # print(l, r, m)
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True

        return False
# @lc code=end
