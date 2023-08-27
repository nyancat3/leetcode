#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap = {num: [] for num in range(1, 10)}
        # T O(n^2)
        for row in range(9):
            for column in range(9):
                digit = board[row][column]
                if digit == '.':
                    continue
                digit = int(digit)
                for coordinate in hashmap[digit]:
                    if not coordinate: break
                    if coordinate[0] == row or coordinate[1] == column or (coordinate[0] // 3 == row // 3 and coordinate[1] // 3 == column // 3):
                        return False
                hashmap[digit].append([row, column])
                # print(hashmap)
        return True
# @lc code=end
