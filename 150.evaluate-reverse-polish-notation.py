#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # O(n)
        for t in tokens:
            if t.lstrip('-').isnumeric():
                stack.append(int(t))
            else:
                # print(stack)
                num_r, num_l = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(num_l + num_r)
                elif t == '-':
                    stack.append(num_l - num_r)
                elif t == '*':
                    stack.append(num_l * num_r)
                elif t == '/':
                    # div = num_l // num_r
                    # div = 0 if div == -1 else div
                    stack.append(int(num_l / num_r))    # python default is decimal division, so have to truncate to zero: -3 // 2 = -1.5 -> -2, int(-1.5) = -1
        return stack[-1]
# @lc code=end
