#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0

        # 1. Read in and ignore any leading whitespace.
        while len(s) > 0 and s[0] == " ":
            s = s[1:len(s)] # Delete a head element
        if len(s) == 0:
            return 0

        # 2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
        res_s = ""
        if s[0] == "-":
            res_s += "-"
        elif s[0].isdecimal():
            res_s += s[0]
        elif s[0] != "+":
            return 0
        # else: # Do nothing if the head letter is "+"

        for each_s in s[1:len(s)]:
            # 3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
            if each_s.isdecimal():
                res_s += each_s
            else:
                break # If the character is not decimal, end reading
        if len(res_s) == 0 or res_s == "-":
            return 0

        # 4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
        res = int(res_s)
        # 5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
        if res < - (2 ** 31):
            res = - (2 ** 31)
        elif res > 2 ** 31 - 1:
            res = 2 ** 31 - 1
        # 6.Return the integer as the final result.
        return res
# @lc code=end
