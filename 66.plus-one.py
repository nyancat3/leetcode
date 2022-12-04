#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # NeetCode answer. Time complexity O(n)
        round, i = 1, len(digits) - 1
        while round:
            if i == -1:
                digits = [1] + digits
                # digits.insert(0, 1)
                round = 0
            elif digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                round = 0
            i -= 1
        return digits

        # My first answer. Time complexity O(2n)? = O(n)
        # ans = 0
        # power = len(digits) - 1
        # for d in digits:
        #     ans += d * 10 ** power
        #     power -= 1
        # ans += 1
        # print(ans)
        # ansList = []
        # while ans:
        #     ansList.append(ans % 10)
        #     ans //= 10
        # return ansList[::-1]
# @lc code=end
