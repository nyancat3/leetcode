#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#
# https://leetcode.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (66.91%)
# Likes:    436
# Dislikes: 75
# Total Accepted:    633.4K
# Total Submissions: 946.4K
# Testcase Example:  '3'
#
# Given an integer n, return a string array answer (1-indexed) where:
#
#
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
#
#
#
# Example 1:
# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:
# Input: n = 15
# Output:
# ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
#
#
# Constraints:
#
#
# 1 <= n <= 10^4
#
#
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            fb = ""
            if i % 3 == 0:
                fb = "Fizz"
            if i % 5 == 0:
                fb += "Buzz"
            if fb:
                answer.append(fb)
            else:
                answer.append(str(i))
        return answer
# @lc code=end
