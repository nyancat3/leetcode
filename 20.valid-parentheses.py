#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str):
        # Better solution: average time complexity is O(n), worst one is O(n^2)
        if len(s) % 2 == 1:
            return False
        dict = {")": "(", "}": "{", "]": "["}
        stack = []
        for s_each in s:    # O(n)
            if s_each in dict: # avg: O(1), worst: O(n)
                if len(stack) == 0 or stack.pop() != dict[s_each]:
                    return False
            else:
                stack.append(s_each)
        return len(stack) == 0

        # Time complexity: O(6n) ? ~= O(n)
        while "()" in s or "{}" in s or "[]" in s: # O(n) for each in operation?
            s = s.replace("()", "") # O(n) for each replacing operation
            s = s.replace("{}", "")
            s = s.replace("[]", "")
        if len(s) > 0:
            return False
        else:
            return True
# @lc code=end
