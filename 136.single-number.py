#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Time O(n), Space O(1)
        result = 0  # n ^ 0 = n
        for n in nums:
            result ^= n
        return result

        # Time O(n), Space O(n) - not constant space so this is a wrong answer
        # numsSet = set()
        # for n in nums:
        #     if n in numsSet:
        #         numsSet.remove(n)  # discard(n) is also fine
        #     else:
        #         numsSet.add(n)
        # return numsSet.pop()
# @lc code=end
