#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [""] * numRows # numRows' length of ["", "", ... ,""]
        if numRows == 1 or len(s) <= numRows:
            return s

        division = numRows + (numRows - 2)
        # TRASH!
        # if numRows == 2:
        #     division = 2
        # elif numRows % 2 == 0: # even
        #     division = numRows + (numRows - 1)
        # else: # odd
        #     division = numRows + (numRows - 2)

        # O(n) solution
        for i in range(len(s)):
            remainder = i % division
            if remainder == 0: # if the string must be the top position
                res[remainder] += s[i]
            elif remainder == division / 2: # if the string must be the bottom position
                res[remainder] += s[i]
            elif i % division > division / 2: # if the string must be straight down from the top
                res[division - i % division] += s[i]
            else: # if the string must be zigzag from bottom up
                res[i % division] += s[i]
        return "".join(res) # Join elements with the specified string. Use empty string this time, it means no connecters
# @lc code=end
