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

        # O(n) solution
        # division = numRows + (numRows - 2)
        # for i in range(len(s)):
        #     remainder = i % division
        #     if remainder == 0: # if the string must be the top position
        #         res[remainder] += s[i]
        #     elif remainder == division / 2: # if the string must be the bottom position
        #         res[remainder] += s[i]
        #     elif i % division > division / 2: # if the string must be straight down from the top
        #         res[division - i % division] += s[i]
        #     else: # if the string must be zigzag from bottom up
        #         res[i % division] += s[i]

        # Smarter O(n) solution learnt from https://leetcode.com/problems/zigzag-conversion/discuss/3404/Python-O(n)-Solution-in-96ms-(99.43)
        row_index, step = 0, 1
        for each_s in s:
            res[row_index] += each_s
            if row_index == 0: # if the string must be the top position or straight down from the top
                step = 1
            elif row_index == numRows - 1: # if the string must be zigzag from bottom up
                step = -1
            # else: do nothing
            row_index += step
        return "".join(res) # Join elements with the specified string. Use empty string this time, it means no connecters
# @lc code=end
