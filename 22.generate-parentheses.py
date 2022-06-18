#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # stack = []
        res = []

        # Backtracking using recursive function
        def backtrack(left_n: int, right_n: int, string: str):
            if left_n == right_n == n:
                res.append(string)
                return
            if left_n < n:
                # stack.append("(")
                backtrack(left_n + 1, right_n, string + "(")
            if left_n > right_n:
                # stack.append(")")
                backtrack(left_n, right_n + 1, string + ")")

        backtrack(0, 0, "")
        return res
# @lc code=end
